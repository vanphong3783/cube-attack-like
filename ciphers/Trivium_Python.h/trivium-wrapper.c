#include <Python.h>
#include "trivium.h"

static int rounds(const u8 *iv, const u8 *key, u16 num_rounds) {
	ECRYPT_ctx ctx = {0};
	u16 rounds_32bits = num_rounds / 32;
	u8 state[4] = {0};
	u16 i, j;

	ECRYPT_keysetup(&ctx, key, 80, 80);
	ECRYPT_ivsetup(&ctx, iv, rounds_32bits);
	ECRYPT_process_bytes(&ctx, state, state, 4);

	i = 3 - ((num_rounds - 32 * rounds_32bits) / 8);
	j = 7 - ((num_rounds - 32 * rounds_32bits) % 8);

	if (state[i] & (1 << j))
		return 1;
	else
		return 0;
}

static inline int seq2array(const PyObject *seq, u8 *arr) {
	u8 i, j;
	PyObject *item;

	for(i = 0; i < 10; i++) {
		arr[i] = 0;
		for (j = 0; j < 8; j++) {
			item = PySequence_Fast_GET_ITEM(seq, 8 * i + j);
			if(!item)
				return 1;

			arr[i] |= (((u8)PyInt_AsUnsignedLongMask(item)) << j);
		}
	}

	return 0;
}	

static PyObject *trivium_rounds(PyObject *self, PyObject *args) {
	u8 iv[10], key[10];
	u16 num_rounds;
	PyObject *iv_seq, *key_seq;

	if (!PyArg_ParseTuple(args, "OOH", &iv_seq, &key_seq, &num_rounds))
		return NULL;

	iv_seq = PySequence_Fast(iv_seq, "IV must be iterable.");
	if (!iv_seq)
		return NULL;
 	if (80 != PySequence_Fast_GET_SIZE(iv_seq)) {
		Py_DECREF(iv_seq);
		return NULL;
	}
	if (seq2array(iv_seq, iv)) {
		Py_DECREF(iv_seq);
		return NULL;
	}
	Py_DECREF(iv_seq);

	key_seq = PySequence_Fast(key_seq, "KEY must be iterable.");
	if (!key_seq)
		return NULL;
	if (80 != PySequence_Fast_GET_SIZE(key_seq)) {
		Py_DECREF(key_seq);
		return NULL;
	}
	if (seq2array(key_seq, key)) {
		Py_DECREF(key_seq);
		return NULL;
	}
	Py_DECREF(key_seq);

	return Py_BuildValue("i", rounds(iv, key, num_rounds));
}

static PyMethodDef TriviumMethods[] = {
	{"rounds",  trivium_rounds, METH_VARARGS, "Trivium with reduced rounds."},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC inittrivium(void) {
	(void) Py_InitModule("trivium", TriviumMethods);
}
