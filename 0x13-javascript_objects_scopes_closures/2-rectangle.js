#!/usr/bin/node

class Rectangles {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || h !== 'number') {
      return {}; //return empty object
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangles;
