#ifndef __TRIVIUM_H__
#define __TRIVIUM_H__

#include "ecrypt-portable.h"

typedef struct
{
  u32 keylen;
  u32 ivlen;

  u8 s[40];
  u8 key[10];

} ECRYPT_ctx;

void ECRYPT_keysetup(
	ECRYPT_ctx* ctx, 
	const u8* key, 
	u32 keysize,
	u32 ivsize);

void ECRYPT_ivsetup(
	ECRYPT_ctx* ctx, 
	const u8* iv,
	const int rounds);

void ECRYPT_process_bytes(
	ECRYPT_ctx* ctx, 
	const u8* input, 
	u8* output, 
	u32 msglen);

#endif /* __TRIVIUM_H__ */