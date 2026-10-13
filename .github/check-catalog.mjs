import assert from 'node:assert/strict';
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';

const root = process.cwd();
const read = path => readFileSync(resolve(root, path), 'utf8');
const slugs = readdirSync(resolve(root, 'docs/mcp')).filter(name => name.endsWith('.md'));
const registrations = new Map();
const adsRegistrations = new Set();
const seenNames = new Set();
let total = 0;
const stripCode = text => text.replace(/^```[^\n]*\n[\s\S]*?^```\s*$/gm, '');
const slug = text => text.toLowerCase().replace(/[`*]/g, '').replace(/[^\p{L}\p{N}_ -]/gu, '').replace(/ /g, '-');

function validateRefs(value, schema, context) {
  if (!value || typeof value !== 'object') return;
  if (typeof value.$ref === 'string' && value.$ref.startsWith('#/')) {
    let target = schema;
    for (const token of value.$ref.slice(2).split('/')) {
      const key = token.replace(/~1/g, '/').replace(/~0/g, '~');
      assert(target && Object.hasOwn(target, key), `${context}: unresolved ${value.$ref}`);
      target = target[key];
    }
  }
  for (const child of Object.values(value)) validateRefs(child, schema, context);
}

for (const file of slugs) {
  const path = `docs/mcp/${file}`;
  const text = read(path);
  const matches = [...text.matchAll(/^### `([^`]+)`\n([\s\S]*?)(?=^### `|^## |$(?![\s\S]))/gm)];
  const count = Number(text.match(/\*\*Inventory:\*\* (\d+) tools\./)?.[1]);
  assert.equal(matches.length, count, `${path}: inventory count`);
  assert(count > 0, `${path}: empty catalog`);
  const defaultCount = Number(text.match(/\*\*Default tools\/list:\*\* (\d+)/)?.[1]);
  assert(defaultCount >= 0 && defaultCount <= count, `${path}: default count`);
  const localNames = new Set();
  const otherStart = text.search(/^## (Other platform tools|Protocol test tools)$/m);
  for (const match of matches) {
    const [, name, body] = match;
    assert(!localNames.has(name), `${path}: duplicate ${name}`);
    localNames.add(name);
    seenNames.add(name);
    const schemaMatches = [...body.matchAll(/^```json\n([\s\S]*?)\n```/gm)];
    assert.equal(schemaMatches.length, 1, `${path}:${name}: exactly one full input schema`);
    const schema = JSON.parse(schemaMatches[0][1]);
    assert.equal(schema.type, 'object', `${path}:${name}: input object schema`);
    validateRefs(schema, schema, `${path}:${name}`);
    const anchor = `tool-${name.toLowerCase().replaceAll('_', '-')}`;
    assert(text.includes(`<a id="${anchor}"></a>`), `${path}:${name}: missing anchor`);
    const target = `${file}#${anchor}`;
    registrations.set(target, name);
    if (otherStart < 0 || match.index < otherStart) adsRegistrations.add(target);
    assert(/\[Source\]\(https:\/\/github\.com\/[^)]+\/blob\/[0-9a-f]{40}\/[^)]+#L\d+\)/.test(body), `${path}:${name}: missing pinned source`);
    assert(body.includes('<summary>Parameters — full input schema</summary>'), `${path}:${name}: missing parameter panel`);
    total++;
  }
  // Each category's navigation count matches the tools under that heading.
  for (const [, title, number] of text.matchAll(/^- \[([^\]]+) \((\d+)\)\]\(#[^)]+\)$/gm)) {
    const categoryText = text.split(`## ${title}\n`)[1]?.split('\n## ')[0];
    assert(categoryText !== undefined, `${path}: missing category ${title}`);
    assert.equal([...categoryText.matchAll(/^### `/gm)].length, Number(number), `${path}: ${title} count`);
  }
}

const index = read('docs/TOOLS.md');
const indexCounts = index.match(/\*\*(\d+) unique names · (\d+) tool registrations · (\d+) MCP servers\.\*\*/);
assert(indexCounts, 'Tool index counts missing');
assert.equal(Number(indexCounts[1]), seenNames.size, 'Tool index unique count');
assert.equal(Number(indexCounts[2]), total, 'Tool index registration count');
assert.equal(Number(indexCounts[3]), slugs.length, 'Tool index provider count');
const indexed = new Map();
const indexedNames = [];
for (const [, name, links] of index.matchAll(/^\| `([^`]+)` \| ([^\n]+) \|$/gm)) {
  indexedNames.push(name);
  for (const [, target] of links.matchAll(/\]\(mcp\/([^)]+)\)/g)) {
    assert.equal(registrations.get(target), name, `Tool index mismatch: ${name} -> ${target}`);
    assert(!indexed.has(target), `Duplicate index link: ${target}`);
    indexed.set(target, name);
  }
}
assert.deepEqual(indexedNames, [...seenNames].sort(), 'Every tool name appears once, alphabetically');
assert.equal(indexed.size, registrations.size, 'Every provider/tool pair is indexed');

const main = read('README.md');
const mainCounts = main.match(/\*\*(\d+) MCP servers · (\d+) tool registrations · (\d+) unique tool names\.\*\*/);
assert(mainCounts, 'README counts missing');
assert.deepEqual(mainCounts.slice(1).map(Number), [slugs.length, total, seenNames.size], 'README counts');
const scopeCounts = main.match(/(\d+) registrations serve Google Ads or shared helpers; (\d+) other-platform or protocol-test tools/);
assert(scopeCounts, 'README scope counts missing');
assert.deepEqual(scopeCounts.slice(1).map(Number), [adsRegistrations.size, total - adsRegistrations.size], 'README Google Ads and other-tool counts');
for (const [, target] of main.matchAll(/\]\(docs\/mcp\/([^)]+#[^)]+)\)/g)) {
  assert(adsRegistrations.has(target), `README promotes a non-Ads tool: ${target}`);
}
for (const [, count, target] of main.matchAll(/\[(\d+) tools\]\(docs\/mcp\/([^)]+)\)/g)) {
  const number = [...registrations.keys()].filter(key => key.startsWith(`${target}#`)).length;
  assert.equal(Number(count), number, `README provider count: ${target}`);
}
const groupLinks = [...main.matchAll(/^- \[([^\]]+) \((\d+)\)\]\(#[^)]+\)$/gm)];
for (const [, title, number] of groupLinks) {
  if (title === 'Full MCP tool catalogs' || title === 'Command-line tools' || title === 'SDKs and client libraries') continue;
  const body = main.split(`## ${title}\n`)[1]?.split('\n## ')[0];
  assert(body, `README task missing: ${title}`);
  const providers = [...body.matchAll(/^\| \[[^\]]+\]\(#[^)]+\) \|/gm)].length;
  assert.equal(providers, Number(number), `README task count: ${title}`);
}

// Validate local page links and fragments; do not make network requests in CI.
const markdown = ['README.md', 'AGENTS.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'docs/TOOLS.md', ...slugs.map(file => `docs/mcp/${file}`)];
const anchorCache = new Map();
function anchors(path) {
  if (!anchorCache.has(path)) {
    const text = stripCode(readFileSync(path, 'utf8'));
    const ids = [...text.matchAll(/<a id="([^"]+)"/g)].map(match => match[1]);
    const headings = [...text.matchAll(/^#{1,6} (.+)$/gm)].map(match => slug(match[1]));
    anchorCache.set(path, new Set([...ids, ...headings]));
  }
  return anchorCache.get(path);
}
for (const file of markdown) {
  const text = stripCode(read(file));
  for (const [, link] of text.matchAll(/\]\(([^)\s]+)\)/g)) {
    if (/^[a-z]+:/i.test(link)) continue;
    const [page, fragment] = link.split('#');
    const target = page ? resolve(root, dirname(file), page) : resolve(root, file);
    assert(existsSync(target), `${file}: missing ${link}`);
    if (fragment) assert(anchors(target).has(fragment), `${file}: missing anchor ${link}`);
  }
}
console.log(`Catalog passed: ${slugs.length} MCPs, ${total} registrations, ${seenNames.size} searchable names; schemas, counts, source pins, and local links valid.`);
