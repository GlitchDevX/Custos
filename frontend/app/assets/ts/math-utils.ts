export function randomInt(minInclusive: number, maxExclusive: number) {
    return Math.random() * (maxExclusive - minInclusive) + minInclusive;
}
