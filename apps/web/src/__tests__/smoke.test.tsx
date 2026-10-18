import { describe, it, expect } from 'vitest';
import en from '../i18n/en.json';
import hi from '../i18n/hi.json';

function flatten(obj: Record<string, unknown>, prefix = ''): string[] {
  return Object.entries(obj).flatMap(([key, value]) =>
    value !== null && typeof value === 'object'
      ? flatten(value as Record<string, unknown>, `${prefix}${key}.`)
      : [`${prefix}${key}`]
  );
}

describe('translations', () => {
  it('English and Hindi have the same keys', () => {
    expect(flatten(hi).sort()).toEqual(flatten(en).sort());
  });

  it('has no empty strings', () => {
    const empties = (obj: Record<string, unknown>): boolean =>
      Object.values(obj).some((v) =>
        typeof v === 'string' ? v.trim() === '' : v !== null && typeof v === 'object' ? empties(v as Record<string, unknown>) : false
      );
    expect(empties(en)).toBe(false);
    expect(empties(hi)).toBe(false);
  });
});
