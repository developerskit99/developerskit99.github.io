import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const TK = require('../assets/js/tools.js');

const approx = (a, b, tol = 1e-6) => Math.abs(a - b) <= tol;

// --- math basics ---
test('pct/pctChange', () => {
  assert.equal(TK.pct(200, 10), 20);
  assert.ok(Number.isNaN(TK.pct('x', 10)));
  assert.ok(approx(TK.pctChange(100, 150), 50));
  assert.ok(Number.isNaN(TK.pctChange(0, 5)));
});

test('mean/median/mode', () => {
  assert.equal(TK.mean([1, 2, 3, 4]), 2.5);
  assert.equal(TK.median([3, 1, 2]), 2);
  assert.equal(TK.median([1, 2, 3, 4]), 2.5);
  assert.deepEqual(TK.mode([1, 2, 2, 3]), [2]);
  assert.ok(Number.isNaN(TK.mean([])));
});

test('stddev', () => {
  // classic: sample stddev of [2,4,4,4,5,5,7,9] = sqrt(32/7) ≈ 2.138
  assert.ok(approx(TK.stddev([2, 4, 4, 4, 5, 5, 7, 9]), 2.138089935, 1e-6));
  assert.ok(approx(TK.stddev([2, 4, 4, 4, 5, 5, 7, 9], true), 2, 1e-9)); // population
  assert.ok(Number.isNaN(TK.stddev([])));
});

test('gcd/lcm', () => {
  assert.equal(TK.gcd(12, 18), 6);
  assert.equal(TK.lcm(4, 6), 12);
});

test('isPrime/factors', () => {
  assert.equal(TK.isPrime(7), true);
  assert.equal(TK.isPrime(8), false);
  assert.equal(TK.isPrime(1), false);
  assert.deepEqual(TK.factors(12), [1, 2, 3, 4, 6, 12]);
});

test('toFraction + fractionToDecimal roundtrip', () => {
  assert.equal(TK.toFraction(0.75), '3/4');
  assert.equal(TK.fractionToDecimal('3/4'), 0.75);
  assert.equal(TK.fractionToDecimal('1 1/2'), 1.5);
  assert.equal(TK.fractionToDecimal('-3/4'), -0.75);
  assert.ok(Number.isNaN(TK.fractionToDecimal('abc')));
  assert.ok(Number.isNaN(TK.fractionToDecimal('1/0')));
  assert.ok(approx(TK.fractionToDecimal(TK.toFraction(0.3333)), 0.3333, 1e-3));
});

test('toMixed', () => {
  assert.equal(TK.toMixed(1.5), '1 1/2');
  assert.equal(TK.toMixed(5), '5');
  assert.equal(TK.toMixed(NaN), '');
  assert.equal(TK.toMixed(0.75), '3/4');
});

test('toBinary/toHex/toRoman', () => {
  assert.equal(TK.toBinary(10), '1010');
  assert.equal(TK.toHex(255), 'ff');
  assert.equal(TK.toRoman(9), 'IX');
  assert.equal(TK.toRoman(2024), 'MMXXIV');
});

test('randomInt range', () => {
  for (let i = 0; i < 50; i++) {
    const v = TK.randomInt(1, 5);
    assert.ok(Number.isInteger(v) && v >= 1 && v <= 5);
  }
  assert.ok(Number.isNaN(TK.randomInt(5, 1)));
});

test('grade/gpa/cgpa/weightedGrade/finalGradeNeeded', () => {
  assert.deepEqual(TK.grade(85, 100), { pct: 85, letter: 'B' });
  assert.ok(approx(TK.gpa(['A', 'B', 'C']), 3.0));
  assert.ok(approx(TK.cgpa([8, 9]), 8.5));
  assert.ok(approx(TK.weightedGrade([90, 80], [0.6, 0.4]), 86));
  assert.ok(approx(TK.weightedGrade([90, 80], [60, 40]), 86));
  assert.ok(Number.isNaN(TK.weightedGrade([90], [50, 50])));
  assert.ok(Number.isNaN(TK.weightedGrade([], [])));
  // final: current 80, final 30%, target 85 -> (85-80*.7)/.3 = 96.67
  assert.ok(approx(TK.finalGradeNeeded(80, 30, 85), 96.6666667, 1e-3));
  assert.ok(Number.isNaN(TK.finalGradeNeeded(80, 0, 85)));
  assert.ok(Number.isNaN(TK.finalGradeNeeded(80, 150, 85)));
});

test('factorial', () => {
  assert.equal(TK.factorial(5), 120);
  assert.equal(TK.factorial(0), 1);
  assert.ok(Number.isNaN(TK.factorial(-1)));
});

test('quadratic real + complex', () => {
  const r = TK.quadratic(1, -3, 2);
  assert.deepEqual([...r.roots].sort((a, b) => a - b), [1, 2]);
  assert.equal(r.disc, 1);
  const c = TK.quadratic(1, 0, 1);
  assert.equal(c.disc, -4);
  assert.deepEqual(c.roots, []);
  assert.ok(c.error.length > 0);
});

test('quadratic edge cases: repeated root, a=0, large discriminant', () => {
  // repeated root: x^2 - 4x + 4 = (x-2)^2 => disc=0, root=2
  const rep = TK.quadratic(1, -4, 4);
  assert.equal(rep.disc, 0);
  assert.ok(approx(rep.roots[0], 2));
  // a=0 is not a quadratic => error
  const a0 = TK.quadratic(0, -5, 6);
  assert.ok(a0.error.length > 0);
  // two distinct real roots: x^2 + x - 6 = (x+3)(x-2)
  const dr = TK.quadratic(1, 1, -6);
  assert.equal(dr.disc, 25);
  assert.deepEqual([...dr.roots].sort((a, b) => a - b), [-3, 2]);
});

test('pctDecrease: correct sign and edge cases', () => {
  // 100 -> 80 = 20% decrease
  assert.ok(approx(TK.pctDecrease(100, 80), 20));
  // equal values = 0% decrease
  assert.ok(approx(TK.pctDecrease(50, 50), 0));
  // decrease to zero = 100%
  assert.ok(approx(TK.pctDecrease(200, 0), 100));
  // zero denominator = NaN
  assert.ok(Number.isNaN(TK.pctDecrease(0, 50)));
  // non-finite inputs = NaN
  assert.ok(Number.isNaN(TK.pctDecrease('abc', 50)));
  assert.ok(Number.isNaN(TK.pctDecrease(100, 'xyz')));
  // small values
  assert.ok(approx(TK.pctDecrease(10, 5), 50));
  // 1000 -> 900 = 10%
  assert.ok(approx(TK.pctDecrease(1000, 900), 10));
});

test('binaryCalc: all operators and edge cases', () => {
  // addition: 1010 + 0011 = 1101
  const add = TK.binaryCalc('1010 + 0011');
  assert.ok(add);
  assert.equal(add.result, 13);
  assert.equal(add.binResult, '1101');
  // subtraction: 1100 - 0011 = 1001
  const sub = TK.binaryCalc('1100 - 0011');
  assert.ok(sub);
  assert.equal(sub.result, 9);
  assert.equal(sub.binResult, '1001');
  // multiplication: 101 * 11 = 1111 (5*3=15)
  const mul = TK.binaryCalc('101 * 11');
  assert.ok(mul);
  assert.equal(mul.result, 15);
  // division: 1100 / 100 = 11 (12/4=3)
  const div = TK.binaryCalc('1100 / 100');
  assert.ok(div);
  assert.equal(div.result, 3);
  // division by zero
  const div0 = TK.binaryCalc('101 / 0');
  assert.ok(!div0);
  // invalid format
  assert.ok(!TK.binaryCalc(''));
  assert.ok(!TK.binaryCalc('abc + 101'));
  assert.ok(!TK.binaryCalc('101 + '));
  assert.ok(!TK.binaryCalc('12 + 101')); // invalid binary char
});

test('toBinary: negative numbers use sign prefix not unsigned', () => {
  // -1 should show "-1" not "4294967295"
  assert.equal(TK.toBinary(-1), '-1');
  assert.equal(TK.toBinary(0), '0');
  assert.equal(TK.toBinary(10), '1010');
  assert.equal(TK.toBinary(255), '11111111');
  assert.equal(TK.toBinary(-5), '-101');
  assert.equal(TK.toBinary(NaN), '');
});

test('bmi: value and WHO categories', () => {
  const r = TK.bmi(70, 175);
  assert.ok(approx(r.value, 22.857, 1e-3));
  assert.equal(r.category, 'Normal weight');
  assert.equal(TK.bmi(50, 175).category, 'Underweight');
  assert.equal(TK.bmi(90, 175).category, 'Overweight');
  assert.equal(TK.bmi(100, 170).category, 'Obese');
  assert.ok(Number.isNaN(TK.bmi(0, 175).value));
  assert.ok(Number.isNaN(TK.bmi(70, 0).value));
  assert.ok(Number.isNaN(TK.bmi(-70, 175).value));
});

test('safeEval', () => {
  assert.equal(TK.safeEval('2+3*4').result, 14);
  assert.equal(TK.safeEval('2+3*4').ok, true);
  assert.equal(TK.safeEval('process.exit()').ok, false);
  assert.equal(TK.safeEval('window.x').ok, false);
  assert.equal(TK.safeEval('abc();').ok, false);
});

test('conversions', () => {
  assert.ok(approx(TK.convertLength(1, 'km', 'm'), 1000));
  assert.ok(Number.isNaN(TK.convertLength(1, 'km', 'zzz')));
  assert.ok(approx(TK.convertWeight(1, 'kg', 'g'), 1000));
  assert.ok(approx(TK.convertTemp(0, 'c', 'f'), 32));
  assert.ok(approx(TK.convertTemp(32, 'f', 'c'), 0));
  assert.ok(approx(TK.convertTemp(0, 'c', 'k'), 273.15));
});

// --- dates ---
test('age object', () => {
  const a = TK.age('2000-03-15');
  assert.equal(typeof a, 'object');
  assert.ok(a !== null);
  for (const k of ['years', 'months', 'days', 'totalDays']) assert.ok(k in a);
  // independent calendrical recompute
  const dob = new Date('2000-03-15'), now = new Date();
  let y = now.getFullYear() - dob.getFullYear(), m = now.getMonth() - dob.getMonth(), d = now.getDate() - dob.getDate();
  if (d < 0) { m--; d += new Date(now.getFullYear(), now.getMonth(), 0).getDate(); }
  if (m < 0) { y--; m += 12; }
  assert.equal(a.years, y);
  assert.equal(a.months, m);
  assert.equal(a.days, d);
  assert.ok(m >= 0 && m <= 11);
  assert.equal(a.totalDays, Math.floor((now - dob) / 86400000));
  assert.equal(TK.age('2999-01-01'), null);
  assert.equal(TK.age('not-a-date'), null);
  assert.equal(TK.age(''), null);
});

test('date utils', () => {
  assert.ok(approx(TK.dateDiff('2024-01-01', '2024-01-11'), 10));
  assert.equal(TK.businessDays('2024-01-01', '2024-01-07'), 5); // Mon-Sun week
  assert.equal(TK.addDays('2024-01-01', 10), '2024-01-11');
  assert.ok(TK.duration(90061000).includes('1d'));
  assert.equal(TK.isLeap(2024), true);
  assert.equal(TK.isLeap(2023), false);
  assert.equal(TK.dayOfWeek('2024-01-01'), 'Monday');
  assert.equal(TK.weekNumber('2024-01-01'), 1);
});

// --- finance ---
test('interest/emi', () => {
  assert.equal(TK.simpleInterest(1000, 5, 2), 100);
  assert.ok(TK.compoundInterest(1000, 10, 1, 1) > 0);
  const emi = TK.emi(500000, 8.5, 60);
  const P = 500000, r = 8.5 / 12 / 100, N = 60;
  const expected = P * r * Math.pow(1 + r, N) / (Math.pow(1 + r, N) - 1);
  assert.ok(approx(emi, expected, 1e-6));
  assert.ok(Math.abs(emi - 10258.27) < 1, `emi=${emi}`);
});

test('finance misc', () => {
  assert.ok(approx(TK.cagr(100, 200, 1), 100));
  assert.ok(TK.sip(1000, 12, 12) > 12000);
  assert.ok(approx(TK.inflation(100, 5, 1), 105));
  assert.equal(TK.discount(100, 20), 80);
  assert.ok(approx(TK.margin(80, 100), 20));
  assert.equal(TK.markup(100, 20), 120);
  const tip = TK.tip(100, 15, 2);
  assert.equal(tip.tip, 15);
  assert.equal(tip.total, 115);
  assert.equal(tip.perPerson, 57.5);
  assert.ok(approx(TK.salary(120000, 12), 10000));
  assert.equal(TK.tax(1000, 20), 200);
  assert.equal(TK.budget(5000, [1000, 2000]), 2000);
  assert.equal(TK.netWorth([5000, 2000], [1000]), 6000);
});

test('business metrics', () => {
  assert.ok(approx(TK.roi(150, 100), 50));
  assert.equal(TK.roas(400, 100), 4);
  assert.ok(approx(TK.conversionRate(5, 100), 5));
  assert.ok(approx(TK.ctr(5, 100), 5));
  assert.equal(TK.cpm(100, 20000), 5);
  assert.equal(TK.cpc(100, 20), 5);
  assert.equal(TK.cac(100, 20), 5);
  assert.equal(TK.clv(10, 2, 3), 60);
  assert.ok(approx(TK.churn(5, 100), 5));
  assert.ok(approx(TK.growthRate(100, 150), 50)); // old,new order
  assert.ok(approx(TK.profitMargin(100, 80), 20));
  const mm = TK.markupVsMargin(80, 100);
  assert.ok(approx(mm.markup, 25));
  assert.ok(approx(mm.margin, 20));
  assert.equal(TK.turnover(100, 50), 2);
  assert.equal(TK.commission(1000, 5), 50);
  assert.equal(TK.breakEven(1000, 10, 6), 250);
  assert.ok(approx(TK.freelanceRate(100000, 1000), 100));
  assert.ok(Number.isNaN(TK.cac(100, 0)));
  assert.ok(Number.isNaN(TK.ctr(1, 0)));
  assert.ok(Number.isNaN(TK.churn(1, 0)));
  assert.ok(Number.isNaN(TK.growthRate(0, 5)));
});

// --- text ---
test('wordCount/toSlug/textDiff', () => {
  const w = TK.wordCount('Hello world. Foo!');
  assert.equal(w.words, 3);
  assert.equal(TK.toSlug('Hello World! 123'), 'hello-world-123');
  const d = TK.textDiff('a\nb', 'a\nc');
  assert.ok(d.some((x) => x.type === 'removed' && x.text === 'b'));
  assert.ok(d.some((x) => x.type === 'added' && x.text === 'c'));
});

test('markdownBasic XSS escape', () => {
  const out = TK.markdownBasic('<script>alert(1)</script>');
  assert.ok(!out.includes('<script>'));
  assert.ok(out.includes('&lt;script&gt;'));
});

test('toAscii/removeDuplicates/sortLines', () => {
  assert.equal(TK.toAscii('AB'), '65 66');
  assert.equal(TK.removeDuplicates('a\nb\na'), 'a\nb');
  assert.equal(TK.sortLines('b\na'), 'a\nb');
  assert.equal(TK.sortLines('a\nb', true), 'b\na');
});

// --- encoding/data ---
test('base64/url/html roundtrips', () => {
  const s = 'Hello, 世界! 123';
  assert.equal(TK.base64Decode(TK.base64Encode(s)), s);
  assert.equal(TK.urlDecode(TK.urlEncode(s)), s);
  assert.equal(TK.htmlDecode(TK.htmlEncode('<b>"hi"&</b>')), '<b>"hi"&</b>');
});

test('yaml roundtrip', () => {
  const p = TK.yamlParse('name: bob\nage: 30\n');
  assert.equal(p.ok, true);
  assert.equal(p.data.name, 'bob');
  assert.equal(p.data.age, 30);
  const str = TK.yamlStringify({ a: 1, b: [1, 2] });
  const back = TK.yamlParse(str);
  assert.equal(back.ok, true);
  assert.equal(back.data.a, 1);
});

test('csv quoted + roundtrip', () => {
  const p = TK.csvParse('a,b\n"x,y",2\n');
  assert.equal(p.ok, true);
  assert.equal(p.data[1][0], 'x,y');
  const rows = [['a', 'b,c'], ['d', 'e']];
  const s = TK.csvStringify(rows);
  const back = TK.csvParse(s);
  assert.deepEqual(back.data, rows);
});

test('xmlValidate', () => {
  assert.equal(TK.xmlValidate('<note><to>Tove</to></note>').ok, true);
  assert.equal(TK.xmlValidate('<note><unclosed>').ok, false);
  assert.equal(TK.xmlValidate('').ok, false);
});

test('validateCron', () => {
  assert.equal(TK.validateCron('*/5 * * * *').ok, true);
  assert.equal(TK.validateCron('bad cron').ok, false);
});

test('regexTest', () => {
  const r = TK.regexTest('\\d+', 'g', 'a1b22');
  assert.equal(r.ok, true);
  assert.equal(r.matches.length, 2);
  const bad = TK.regexTest('x', 'zz', 'abc');
  assert.equal(bad.ok, false);
  assert.match(bad.error, /Bad flags/);
});

test('lorem counts', () => {
  assert.equal(TK.lorem('words', 5).split(' ').length, 5);
  assert.ok(TK.lorem('sentences', 2).length > 0);
  assert.ok(TK.lorem('paragraphs', 2).length > 0);
});

// --- minifiers ---
test('cssMinify protects strings', () => {
  const out = TK.cssMinify('a{content:"{";color:red}/*c*/ b{background:url("https://x.com/a")}');
  assert.ok(out.includes('"{"'), out);
  assert.ok(out.includes('https://x.com/a'), out);
  assert.ok(!out.includes('/*c*/'));
});

test('jsMinify protects strings', () => {
  const out = TK.jsMinify('const u = "https://x.com/a"; // comment\nvar x=1;');
  assert.ok(out.includes('"https://x.com/a"'), out);
  assert.ok(!out.includes('// comment'));
  assert.ok(!out.includes('https://x.com/a"; //'), out);
});

// --- color ---
test('color roundtrips', () => {
  assert.deepEqual(TK.hexToRgb('#ff0000'), { r: 255, g: 0, b: 0 });
  assert.equal(TK.rgbToHex(255, 0, 0), '#ff0000');
  const hsl = TK.rgbToHsl(255, 0, 0);
  const rgb = TK.hslToRgb(hsl.h, hsl.s, hsl.l);
  assert.ok(Math.abs(rgb.r - 255) <= 2 && Math.abs(rgb.g) <= 2 && Math.abs(rgb.b) <= 2);
});

test('palette/contrast/colorName', () => {
  assert.equal(TK.palette('#ff0000').length, 4);
  assert.equal(TK.contrastRatio('#000000', '#ffffff'), 21);
  assert.equal(TK.colorName('#ff0000'), 'Red');
});

// --- new builders ---
test('markdownTable shape', () => {
  const t = TK.markdownTable(2, 2, true);
  const lines = t.split('\n');
  assert.equal(lines.length, 4); // header + sep + 2 rows
  for (const l of lines) assert.ok(l.startsWith('|') && l.endsWith('|'));
  const noH = TK.markdownTable(2, 2, false);
  assert.equal(noH.split('\n').length, 2);
  const def = TK.markdownTable();
  assert.ok(def.includes('Header 1'));
});

test('asciiArt', () => {
  const a = TK.asciiArt('Hi');
  assert.ok(typeof a === 'string' && a.length > 0);
  assert.equal(a.split('\n').length, 5);
  assert.ok(a.includes('█'));
});

test('primes/scientific/proportion', () => {
  assert.deepEqual(TK.primesUpTo(20), [2, 3, 5, 7, 11, 13, 17, 19]);
  const sci = TK.toScientific(123456);
  assert.equal(sci, (123456).toExponential(2));
  assert.ok(approx(TK.fromScientific(sci), 123456, 1000)); // 2dp mantissa => lossy
  assert.equal(TK.fromScientific(TK.toScientific(100000)), 100000);
  assert.ok(Number.isNaN(TK.fromScientific('zzz')));
  assert.equal(TK.solveProportion(2, 4, 3), 6);
  assert.ok(Number.isNaN(TK.solveProportion(0, 4, 3)));
});
