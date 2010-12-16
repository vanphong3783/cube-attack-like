#include "trivium.h"

//static u8 reverse(u8 x)
//{
//	return ((x         << 7) | ((x & 0x02) << 5) | ((x & 0x04) << 3) | ((x & 0x08) << 1) | 
//		   ((x & 0x10) >> 1) | ((x & 0x20) >> 3) | ((x & 0x40) >> 5) | ((x & 0x80) >> 7));
//}

int rounds(const u8* iv, const u8* key, const int rounds)
{
	ECRYPT_ctx ctx = {0};
	int rounds_32bits = rounds / 32;
	u8 state[4] = {0};
	int i;
	int j;

	ECRYPT_keysetup(&ctx, key, 80, 80);
	ECRYPT_ivsetup(&ctx, iv, rounds_32bits);
	ECRYPT_process_bytes(&ctx, state, state, 4);

	i = 3 - (rounds - 32 * rounds_32bits) / 8;
	j = 7 - ((rounds - 32 * rounds_32bits) % 8);

//	return reverse(state[i]);

	if (state[i] & (1 << j))
		return 1;
	else
		return 0;
}

//int full(const u8* key, const u8* iv)
//{
//	return rounds(key, iv, 1152);
//}
