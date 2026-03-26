export function fromPath(pathArr) {
  if (!Array.isArray(pathArr)) {
    return String(pathArr);
  }

  let pathString = '';
  for (let i = 0; i < pathArr.length; i++) {
    const segment = pathArr[i];
    if (typeof segment === 'number' || (typeof segment === 'string' && /^\d+$/.test(segment))) {
      // Use bracket notation for array indices
      pathString += `[${segment}]`;
    } else {
      // Use dot notation for object properties
      if (i > 0) {
        pathString += '.';
      }
      pathString += segment;
    }
  }
  return pathString;
}
