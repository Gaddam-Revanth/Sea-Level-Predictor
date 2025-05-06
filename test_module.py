import unittest
from sea_level_predictor import draw_plot
import matplotlib

matplotlib.use('Agg')  # Use non-interactive backend for testing

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot_exists(self):
        fig = draw_plot()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()