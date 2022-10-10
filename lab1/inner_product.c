#define LEN 10

int inner_product(int *v1, int *v2, int len) {
  return len != 0 ? *v1 * *v2 + inner_product(v1 + 1, v2 + 1, len - 1) : 0;
}

int main() {
  int v1[LEN] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int v2[LEN] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
  int res = inner_product(v1, v2, LEN); // should return 952
  return res; // run `echo $?` in bash to check if the return value equals to
              // (952 % 256) = 184?
}