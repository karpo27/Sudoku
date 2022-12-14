top_left = "╔"
top_right = "╗"
bot_left = "╚"
bot_right = "╝"

top_middle = "╤"
mid_center = "┼"
bot_middle = "╧"
top_middle_t = "╦"
bot_middle_b = "╩"
mid_center_tb = "╬"
mid_center_m = "╪"

mid_left = "╟"
mid_right = "╢"
mid_left_tb = "╠"
mid_right_tb = "╣"

h_line = "──" * 3
v_line = "│"
h_line_tb = "══" * 3
v_line_tb = "║"

space_1 = "  1   "  # 6 spaces
space_2 = "  2   "
space_3 = "  3   "
space_4 = "  4   "
space_5 = "  5   "
space_6 = "  6   "
space_7 = "  7   "
space_8 = "  8   "
space_9 = "  9   "

example_board_box = " " + top_left + h_line_tb + top_middle + h_line_tb + top_middle + h_line_tb + top_right + "\n"\
        " " + v_line_tb + space_1 + v_line + space_2 + v_line + space_3 + v_line_tb + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line_tb + space_4 + v_line + space_5 + v_line + space_6 + v_line_tb + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line_tb + space_7 + v_line + space_8 + v_line + space_9 + v_line_tb + "\n"\
        " " + bot_left + h_line_tb + bot_middle + h_line_tb + bot_middle + h_line_tb + bot_right + "\n"\

h_line_2 = "──" * 2
h_line_tb_2 = "══" * 2

space_1_2 = " 1  "  # 2 spaces
space_2_2 = " 2  "
space_3_2 = " 3  "
space_4_2 = " 4  "
space_5_2 = " 5  "
space_6_2 = " 6  "
space_7_2 = " 7  "
space_8_2 = " 8  "
space_9_2 = " 9  "

top_line = top_left + ((h_line_tb_2 + top_middle) * 2 + h_line_tb_2 + top_middle_t) * 2 + (h_line_tb_2 + top_middle) * 2 + h_line_tb_2 + top_right
mid_line_1 = v_line_tb + (space_1_2 + v_line + space_2_2 + v_line + space_3_2 + v_line_tb) * 3
mid_line_2 = v_line_tb + (space_4_2 + v_line + space_5_2 + v_line + space_6_2 + v_line_tb) * 3
mid_line_3 = v_line_tb + (space_7_2 + v_line + space_8_2 + v_line + space_9_2 + v_line_tb) * 3
mid_line_m = mid_left + (h_line_2 + mid_center + h_line_2 + mid_center + h_line_2 + mid_right) * 3
mid_line_b = mid_left_tb + ((h_line_tb_2 + mid_center_m) * 2 + h_line_tb_2 + mid_center_tb) * 2 + (h_line_tb_2 + mid_center_m) * 2 + h_line_tb_2 + mid_right_tb
bot_line = bot_left + ((h_line_tb_2 + bot_middle) * 2 + h_line_tb_2 + bot_middle_b) * 2 + (h_line_tb_2 + bot_middle) * 2 + h_line_tb_2 + bot_right

example_board_grid = " " + top_line + "\n"\
                " " + mid_line_1 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_2 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_3 + "\n"\
                " " + mid_line_b + "\n"\
                " " + mid_line_1 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_2 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_3 + "\n"\
                " " + mid_line_b + "\n"\
                " " + mid_line_1 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_2 + "\n"\
                " " + mid_line_m + "\n"\
                " " + mid_line_3 + "\n"\
                " " + bot_line + "\n"\

board = " " + top_line + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_m + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_m + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_b + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_m + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_m + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_b + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_m + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + mid_line_m + "\n"\
        " " + v_line_tb + (" {:^2} " + v_line + " {:^2} " + v_line + " {:^2} " + v_line_tb) * 3 + "\n"\
        " " + bot_line

