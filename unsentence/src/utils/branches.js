
export function run_(cb) {
    return cb()
}

/**
 * @template T
 * @param {T[]} items
 * @returns {(cb: Parameters<Array<T>["map"]>[0]) => void}
 */
export function each_(items) {
    return (cb) => {
        return items.map(cb);
    };
}