exports.esrever = function (list) {
  for (i = 0; i < list.length; i++) {
    const tmp = list.splice(i, 1)[0];
    list.unshift(tmp);
  }
  return list;
}
;