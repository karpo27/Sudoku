top_left = "┌"
top_right = "┐"
bot_left = "└"
bot_right = "┘"

top_middle = "┬"
mid_center = "┼"
bot_middle = "┴"

mid_left = "├"
mid_right = "┤"

h_line = "──" * 3
v_line = "│"

space_1 = "  1   "  # 6 spaces
space_2 = "  2   "
space_3 = "  3   "
space_4 = "  4   "
space_5 = "  5   "
space_6 = "  6   "
space_7 = "  7   "
space_8 = "  8   "
space_9 = "  9   "

example_board_box = " " + top_left + h_line + top_middle + h_line + top_middle + h_line + top_right + "\n"\
                " " + v_line + space_1 + v_line + space_2 + v_line + space_3 + v_line + "\n"\
                " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
                " " + v_line + space_4 + v_line + space_5 + v_line + space_6 + v_line + "\n"\
                " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
                " " + v_line + space_7 + v_line + space_8 + v_line + space_9 + v_line + "\n"\
                " " + bot_left + h_line + bot_middle + h_line + bot_middle + h_line + bot_right + "\n"\

h_line_2 = "──" * 2

space_1_2 = " 1  "  # 2 spaces
space_2_2 = " 2  "
space_3_2 = " 3  "
space_4_2 = " 4  "
space_5_2 = " 5  "
space_6_2 = " 6  "
space_7_2 = " 7  "
space_8_2 = " 8  "
space_9_2 = " 9  "

top_line = (top_left + h_line_2 + top_middle + h_line_2 + top_middle + h_line_2 + top_right) * 3
mid_line_1 = (v_line + space_1_2 + v_line + space_2_2 + v_line + space_3_2 + v_line) * 3
mid_line_2 = (v_line + space_4_2 + v_line + space_5_2 + v_line + space_6_2 + v_line) * 3
mid_line_3 = (v_line + space_7_2 + v_line + space_8_2 + v_line + space_9_2 + v_line) * 3
mid_line_m = (mid_left + h_line_2 + mid_center + h_line_2 + mid_center + h_line_2 + mid_right) * 3
bot_line = (bot_left + h_line_2 + bot_middle + h_line_2 + bot_middle + h_line_2 + bot_right) * 3

example_board_grid = " " + top_line + "\n"\
                " " + mid_line_1 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_2 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_3 + "\n"\
                " " + bot_line + "\n"\



board = " " + top_line + "\n"\
        " " + mid_line_1 + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + bot_left + h_line + bot_middle + h_line + bot_middle + h_line + bot_right + "\n"

print(board)


boards = " " + top_line + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + bot_left + h_line + bot_middle + h_line + bot_middle + h_line + bot_right + "\n"