void test(int z) {
  if (z == 0) {
    int x = 1 / z; // warn
  } else {
    int y = 1 / z; // no warn
  }
}