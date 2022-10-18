/*************************** HEADER FILES ***************************/
#include "crypto.h"
#include <stdio.h>
#include <string.h>

/*********************** FUNCTION DEFINITIONS ***********************/
int crypto_test() {
  // Provide your own test case
  char text[] = {"**************************"};
  char code[] = {"**************************"};
  char buf[1024];
  int pass = 1;

  // Apply `encode` function from libcrytpo.a
  strcpy(buf, text);
  encode(buf);
  pass = pass && !strcmp(code, buf);

  // Apply `decode` function from libcrytpo.a
  decode(buf);
  pass = pass && !strcmp(text, buf);

  return (pass);
}

int main() {
  printf("Crytpo test: %s\n", crypto_test() ? "SUCCEEDED" : "FAILED");

  return (0);
}
