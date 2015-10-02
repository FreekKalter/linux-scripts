import unittest
from cleanupfilename import rename


class TestRename(unittest.TestCase):
    files = []
    dirs = []

    def setUp(self):
        self.files = [('filename-sample.x264.mp4', 'filename.mp4'),
                      ('filename.mp4', 'filename.mp4')]
        self.dirs = [('filename sample mp4', 'filename'),
                     ('filename 540p', 'filename'),
                     ('filename [web-DL] part001.', 'filename'),
                     ('actual.file.name-1080p.BluRay.x264-GECKOS[rarbg]', 'actual file name'),
                     ]

    def test_list(self):
        for file, output in self.files:
            self.assertEqual(rename(file, False), output)
        for file, output in self.dirs:
            self.assertEqual(rename(file, True), output)

if __name__ == '__main__':
    unittest.main()
