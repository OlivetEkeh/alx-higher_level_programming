#!/usr/bin/node

module.exports = class Rectangles {
  constructor(w, h) {
    if (w <= 0 || h <= 0 && typeof w !== 'number' && h !== 'number') {
      this.width = w;
      this.height = h;
    }
  }
}
