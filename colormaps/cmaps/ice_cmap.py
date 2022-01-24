# For using this cmap you have to import the script and preprocess the list with list2list and Ccmap from cmap_tools.py
# Considers changes between ice shelves and accumulation zones
ant_ice_sheet = [225, 224, 233,
                 224, 223, 232,
                 223, 222, 231,
                 222, 221, 230,
                 221, 220, 229,
                 220, 219, 228,
                 219, 218, 227,
                 218, 217, 226,
                 217, 217, 225,
                 216, 216, 223,
                 215, 215, 222,
                 214, 214, 221,
                 213, 213, 220,
                 212, 212, 219,
                 211, 211, 218,
                 210, 210, 217,
                 209, 209, 216,
                 208, 208, 215,
                 207, 207, 214,
                 206, 206, 212,
                 205, 205, 211,
                 204, 204, 210,
                 203, 203, 209,
                 202, 202, 208,
                 201, 201, 207,
                 200, 200, 206,
                 199, 200, 205,
                 198, 199, 204,
                 197, 198, 202,
                 196, 197, 201,
                 195, 196, 200,
                 194, 195, 199,
                 193, 194, 198,
                 192, 193, 197,
                 191, 192, 196,
                 190, 191, 195,
                 189, 190, 194,
                 188, 189, 193,
                 187, 188, 191,
                 186, 187, 190,
                 185, 186, 189,
                 184, 185, 188,
                 183, 184, 187,
                 182, 183, 186,
                 181, 182, 185,
                 180, 182, 184,
                 179, 181, 183,
                 178, 180, 182,
                 177, 179, 180,
                 176, 178, 179,
                 175, 177, 178,
                 174, 176, 177,
                 173, 175, 176,
                 172, 174, 175,
                 171, 173, 174,
                 170, 172, 173,
                 169, 171, 172,
                 168, 170, 170,
                 167, 169, 169,
                 166, 168, 168,
                 165, 167, 167,
                 163, 166, 166,
                 162, 165, 165,
                 161, 165, 164,
                 161, 164, 163,
                 163, 166, 165,
                 164, 167, 166,
                 166, 169, 168,
                 167, 170, 169,
                 169, 171, 171,
                 170, 173, 172,
                 172, 174, 174,
                 173, 176, 175,
                 175, 177, 177,
                 176, 179, 178,
                 178, 180, 179,
                 179, 181, 181,
                 180, 183, 182,
                 182, 184, 184,
                 183, 186, 185,
                 185, 187, 187,
                 186, 189, 188,
                 188, 190, 190,
                 189, 192, 191,
                 191, 193, 193,
                 192, 194, 194,
                 194, 196, 195,
                 195, 197, 197,
                 197, 199, 198,
                 198, 200, 200,
                 200, 202, 201,
                 201, 203, 203,
                 203, 205, 204,
                 204, 206, 206,
                 206, 207, 207,
                 207, 209, 209,
                 209, 210, 210,
                 210, 212, 211,
                 212, 213, 213,
                 213, 215, 214,
                 215, 216, 216,
                 216, 218, 217,
                 218, 219, 219,
                 219, 220, 220,
                 221, 222, 222,
                 222, 223, 223,
                 224, 225, 225,
                 225, 226, 226,
                 227, 228, 227,
                 228, 229, 229,
                 230, 231, 230,
                 231, 232, 232,
                 233, 233, 233,
                 234, 235, 235,
                 236, 236, 236,
                 237, 238, 238,
                 239, 239, 239,
                 240, 241, 241,
                 242, 242, 242,
                 243, 244, 243,
                 245, 245, 245,
                 246, 246, 246,
                 248, 248, 248,
                 249, 249, 249,
                 251, 251, 251,
                 252, 252, 252,
                 254, 254, 254,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 255, 255, 255,
                 254, 255, 255,
                 254, 254, 254,
                 253, 254, 254,
                 253, 253, 254,
                 253, 253, 253,
                 252, 252, 253,
                 252, 252, 252,
                 251, 252, 252,
                 251, 251, 252,
                 250, 251, 251,
                 250, 250, 251,
                 249, 250, 250,
                 249, 250, 250,
                 248, 249, 250,
                 248, 249, 249,
                 247, 248, 249,
                 247, 248, 249,
                 246, 247, 248,
                 246, 247, 248,
                 245, 247, 247,
                 245, 246, 247,
                 244, 246, 247,
                 244, 245, 246,
                 243, 245, 246,
                 243, 244, 245,
                 242, 244, 245,
                 242, 244, 245,
                 241, 243, 244,
                 241, 243, 244,
                 240, 242, 243,
                 240, 242, 243,
                 239, 241, 243,
                 239, 241, 242,
                 238, 241, 242,
                 238, 240, 242,
                 237, 240, 241,
                 237, 239, 241,
                 237, 239, 240,
                 236, 238, 240,
                 236, 238, 240,
                 235, 238, 239,
                 235, 237, 239,
                 234, 237, 238,
                 234, 236, 238,
                 233, 236, 238,
                 233, 236, 237,
                 232, 235, 237,
                 232, 235, 236,
                 231, 234, 236,
                 231, 234, 236,
                 230, 233, 235,
                 230, 233, 235,
                 229, 233, 235,
                 229, 232, 234,
                 228, 232, 234,
                 228, 231, 233,
                 227, 231, 233,
                 227, 230, 233,
                 226, 230, 232,
                 226, 230, 232,
                 225, 229, 231,
                 225, 229, 231]
