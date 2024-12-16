import unittest
from aknak_hf import create_minefiled


class TestAknak_hf(unittest.TestCase):
    def setUp(self):
        global GRID_SIZE, NUM_MINES
        GRID_SIZE = 3
        NUM_MINES = 1

    def test_create_minefield(self):
        grid, mines = create_minefiled(grid_size=GRID_SIZE, num_mines=NUM_MINES)
        self.assertEqual(len(mines), NUM_MINES)
        mine_coiunt = sum(row.count('M') for row in grid)
        self.assertEqual(mine_coiunt, NUM_MINES)


    def test_calculate_numbers(self):
        grid = [
            ['M', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', 'M'],
        ]
        expected = [
            ['M', '1', ' '],
            ['1', '2', '1'],
            [' ', '1', 'M'],
        ]
        calculate_numbers(grid)
        self.assertEqual(grid, expected)

    def test_reveal_cell_number(self):
        grid = [
            ['1', '1', ' '],
            ['1', 'M', ' '],
            ['1', '1', ' '],
        ]
        visible_grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        result = reveal_cell(grid, visible_grid, 0, 0)
        self.assertFalse(result)
        self.assertEqual(visible_grid, [
            ['1', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ])

    def test_reveal_cell_mine(self):
        grid = [
            ['1', '1', ' '],
            ['1', 'M', ' '],
            ['1', '1', ' '],
        ]
        visible_grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        result = reveal_cell(grid, visible_grid, 0, 1)
        self. assertTrue(result)

    def test_reveal_cell_empty(self):
        grid = [
            [' ', '1', ' '],
            [' ', '1', 'M'],
            [' ', ' ', ' '],
        ]
        visible_grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        result = reveal_cell(grid, visible_grid, 0, 0)
        self.assertFalse(result)
        self.assertEqual(visible_grid, [
            [' ', '1', ' '],
            [' ', '1', ' '],
            [' ', ' ', ' '],
        ])

    def test_reveal_cell_with_pread(self):
        grid =[
            [' ', '1', 'M'],
            [' ', '1', '1'],
            [' ', ' ', ' '],
        ]
        visible_grid = [

        ]