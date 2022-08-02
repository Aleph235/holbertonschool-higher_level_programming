#!/user/bin/node

exports.converter = function (base) {
  return function (star) {
    return star.toString(base);
  };
};
