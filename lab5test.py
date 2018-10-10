class TestMidtermPractice:
  def test_remove_leading_blanks(self):
    s1 = "   3 leading blanks removed"
    r1 = "3 leading blanks removed"
    self.assertEqual(self.lab5.remove_leading_blanks(s1), r1)
