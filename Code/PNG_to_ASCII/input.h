/*  GIMP header image file format (INDEXED): C:\Users\Student\Documents\PNG_to_ASCII\input.h  */

static unsigned int width = 64;
static unsigned int height = 64;

/*  Call this macro repeatedly.  After each use, the pixel data can be extracted  */

#define HEADER_PIXEL(data,pixel) {\
pixel[0] = header_data_cmap[(unsigned char)data[0]][0]; \
pixel[1] = header_data_cmap[(unsigned char)data[0]][1]; \
pixel[2] = header_data_cmap[(unsigned char)data[0]][2]; \
data ++; }

static unsigned char header_data_cmap[256][3] = {
	{255,255,255},
	{228,228,228},
	{136,136,136},
	{ 34, 34, 34},
	{252,167,208},
	{225, 16, 16},
	{226,150, 37},
	{158,107, 70},
	{228,218, 54},
	{151,224, 85},
	{ 36,190, 43},
	{ 47,210,220},
	{ 30,130,196},
	{ 22,  0,228},
	{205,109,224},
	{128,  0,125},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255},
	{255,255,255}
	};
static unsigned char header_data[] = {
	3,3,3,3,3,3,3,3,3,3,3,3,3,7,7,7,
	7,7,7,5,5,5,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,7,7,7,7,7,
	7,7,7,7,7,7,5,5,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,7,7,7,7,7,7,
	3,3,7,7,3,7,7,7,7,3,3,3,3,3,3,3,
	3,3,3,5,3,3,5,5,3,3,5,3,5,3,3,5,
	5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,7,7,7,7,7,7,7,
	3,3,7,7,7,7,7,3,7,7,3,3,3,3,3,3,
	5,3,3,5,3,5,3,3,3,3,5,3,5,3,5,3,
	3,3,3,5,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,7,7,7,7,7,7,7,3,
	3,3,7,7,7,7,7,7,3,7,7,3,3,3,3,3,
	5,5,3,5,3,5,5,5,3,3,5,3,5,3,5,5,
	5,3,3,5,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,7,7,7,7,7,7,7,3,3,
	7,7,7,7,7,7,7,7,3,7,7,7,3,3,3,3,
	5,3,5,5,3,5,3,3,3,3,5,5,5,3,5,3,
	3,3,3,5,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,7,7,7,7,7,7,7,7,3,
	7,7,7,7,7,7,7,3,3,7,7,7,7,3,3,3,
	5,3,3,5,3,3,5,5,3,3,3,5,3,3,3,5,
	5,3,3,5,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,7,7,7,7,7,7,7,7,7,7,
	7,7,3,3,3,3,7,3,7,7,7,3,7,5,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,7,7,7,7,7,3,7,7,7,7,
	3,7,7,3,3,7,7,3,7,7,7,7,7,5,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,7,7,7,7,3,3,7,7,7,
	7,7,3,3,7,7,7,3,7,7,7,7,7,5,3,3,
	3,5,5,3,3,3,5,5,3,3,5,3,3,3,5,3,
	3,3,3,5,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,7,7,7,7,7,3,3,3,3,
	3,4,4,4,4,3,7,7,7,3,3,7,7,5,3,3,
	5,3,3,3,3,5,3,3,5,3,5,5,3,3,5,5,
	3,3,5,3,3,5,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,7,7,4,4,7,4,4,4,4,
	4,4,4,4,4,3,7,7,7,7,3,3,7,5,3,3,
	5,3,5,5,3,5,3,3,5,3,5,3,5,3,5,3,
	5,3,5,5,5,5,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,3,3,7,7,3,7,7,5,3,3,
	5,3,3,5,3,5,3,3,5,3,5,3,5,3,5,3,
	5,3,5,3,3,5,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,3,7,7,3,7,7,5,3,3,
	3,5,5,3,3,3,5,5,3,3,5,3,5,3,5,3,
	5,3,5,3,3,5,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,3,3,3,3,7,7,5,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,3,3,7,7,7,5,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,3,3,4,4,4,4,3,
	3,3,3,4,4,4,4,3,3,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,5,3,3,5,5,3,3,3,5,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,2,3,3,3,3,4,4,4,3,3,
	3,3,3,2,3,3,3,3,3,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,5,3,5,3,3,5,3,5,5,
	5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,4,4,3,3,3,3,7,7,5,3,3,3,
	3,3,3,3,3,3,3,5,3,5,5,5,5,3,3,5,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,
	3,3,3,3,4,4,4,4,3,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,5,3,5,3,3,3,3,3,5,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,
	3,3,3,3,4,4,4,4,4,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,5,3,3,5,5,3,3,3,5,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,4,4,4,3,3,
	3,3,3,4,4,4,4,4,4,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,4,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,7,7,7,7,5,3,3,3,
	3,3,3,3,3,3,3,3,3,5,3,3,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,7,7,7,5,3,3,3,3,
	3,3,3,3,3,3,3,3,3,5,3,3,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,7,7,5,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,5,3,3,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,4,5,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,5,3,3,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,4,5,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,5,5,5,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,4,4,5,5,5,5,5,5,
	4,4,4,4,4,4,4,4,4,5,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,4,4,5,5,5,4,4,
	4,4,4,4,4,4,4,4,4,5,3,3,3,3,3,3,
	3,5,5,5,3,3,5,5,5,5,3,5,3,3,3,5,
	3,3,3,3,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,4,5,3,3,3,3,3,3,
	3,5,3,3,5,3,5,3,3,5,3,5,3,3,3,5,
	3,5,3,3,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,2,3,7,3,3,3,3,3,
	3,5,3,3,5,3,5,3,3,5,3,5,3,5,3,5,
	3,5,5,3,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,
	4,4,4,4,4,4,4,4,3,3,3,7,3,3,3,3,
	3,5,3,3,5,3,5,3,3,5,3,3,5,3,5,3,
	3,5,3,5,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,
	4,4,4,4,4,4,4,2,3,12,2,3,7,5,3,3,
	3,5,5,5,3,3,5,5,5,5,3,3,5,3,5,3,
	3,5,3,3,5,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,
	4,4,4,4,4,4,2,3,3,12,12,12,13,13,2,5,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,
	4,4,4,4,4,2,3,3,12,12,12,13,13,13,13,13,
	7,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,2,4,4,
	4,4,4,4,2,3,3,12,12,12,12,12,13,13,13,13,
	13,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,12,2,4,4,
	4,4,2,3,3,3,12,12,12,12,12,12,12,13,13,13,
	13,13,2,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,12,2,4,4,
	2,3,3,3,3,12,12,12,12,12,12,12,12,12,12,13,
	13,13,13,12,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,12,12,2,3,3,
	3,3,3,12,12,12,12,12,12,3,12,12,12,12,12,13,
	13,13,13,13,12,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,11,11,11,12,12,3,3,
	12,12,12,12,12,12,12,12,3,2,12,12,12,12,12,12,
	13,13,13,13,13,2,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,12,11,11,11,11,11,11,12,12,
	12,12,12,12,12,12,12,3,12,12,3,12,12,12,12,12,
	13,13,13,13,13,13,2,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,11,11,11,11,11,11,11,11,12,
	12,12,12,12,12,12,3,12,12,3,2,12,12,12,12,12,
	12,13,13,13,13,13,13,2,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,11,11,11,11,11,12,11,11,11,12,
	12,12,12,12,12,12,12,12,12,3,3,12,12,12,3,3,
	12,12,13,13,13,13,13,13,2,3,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,12,11,11,11,11,11,11,11,11,11,11,
	12,12,12,12,3,12,12,12,12,12,12,12,12,3,2,12,
	12,12,12,13,13,13,13,13,13,2,3,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	12,12,12,3,12,12,12,12,12,12,12,12,12,12,12,12,
	12,12,12,12,13,13,13,13,13,13,7,3,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,12,11,11,11,11,11,11,11,11,11,11,11,
	11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
	12,12,12,12,12,13,13,13,13,13,13,7,3,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,11,
	11,11,12,12,12,12,12,12,12,12,3,12,12,12,12,12,
	12,12,12,12,12,13,13,13,13,13,13,3,5,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,12,12,12,2,12,12,12,3,12,12,12,12,12,
	12,12,12,3,12,12,13,13,13,13,13,13,2,3,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,
	12,12,3,12,12,12,12,13,13,13,13,13,13,15,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,
	12,3,3,12,12,12,3,13,13,13,13,13,13,13,3,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,12,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,12,12,12,2,3,12,12,12,12,12,
	12,3,12,12,12,3,12,12,13,13,13,13,13,13,13,3,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,12,12,12,12,2,12,12,12,12,12,
	12,3,12,12,12,3,12,12,13,13,13,13,13,13,13,15,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,
	12,3,12,12,12,2,12,12,12,13,13,13,13,13,13,13,
	3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,12,12,12,12,12,12,3,12,12,
	12,3,12,12,12,3,12,12,12,13,13,13,13,13,13,13,
	15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,12,12,12,12,12,12,3,12,12,
	12,3,12,12,12,3,12,12,12,12,13,13,13,13,13,13,
	13,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,
	12,3,12,12,12,3,12,12,12,12,13,13,13,13,13,13,
	13,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,
	12,3,2,12,12,3,12,12,12,12,12,13,13,13,13,13,
	13,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,12,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,
	12,3,3,12,12,3,12,12,12,12,12,12,13,13,13,13,
	13,13,15,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,
	12,3,3,12,12,3,2,12,12,3,12,12,13,13,13,13,
	13,13,13,3,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,
	12,3,3,12,12,12,3,12,12,12,12,12,13,13,13,13,
	13,13,13,12,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,
	12,3,3,12,12,12,3,12,12,3,12,12,12,13,13,13,
	13,13,13,13,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,11,11,11,11,11,11,11,11,11,11,11,
	11,11,11,11,12,12,11,11,11,11,12,12,12,12,12,12,
	12,3,3,12,12,12,3,12,12,12,12,12,12,13,13,13,
	13,13,13,15,3,3,3,3,3,3,3,3,3,3,3,3,
	3,3,3,3,3,12,12,12,12,11,11,11,11,11,11,11,
	11,11,11,11,12,12,12,11,11,11,12,12,12,12,12,12,
	12,3,3,12,12,12,3,12,12,3,12,12,12,13,13,13,
	3,3,3,3,7,3,3,3,3,3,3,3,3,3,3,3
	};
