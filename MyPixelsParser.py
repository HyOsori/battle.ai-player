# -*-coding:utf-8-*-
from baseClass.PixelsParser import PixelsParser
import random


class MyPixelsParser(PixelsParser):
    def loop_phase(self):
        '''
        input은 self.game_data에 dict형태로 저장된다.

        input 목록
        width = self.width
        height = self.height
        color_array = self.color_array
        ruler_array = self.ruler_array
        start_point_y = self.game_data['start_point_y']
        start_point_x = self.game_data['start_point_x']
        ruler_self = self.game_data['ruler_self']
        ruler_enemy = self.game_data['ruler_enemy']
        enemy_chosen_color = self.game_data['enemy_chosen_color']

        output 목록
        parsing_data['chosen_color'] : 당신이 변경할 색깔
        :return:
        '''
        start_point_y = self.game_data['start_point_y']
        start_point_x = self.game_data['start_point_x']
        ruler_self = self.game_data['ruler_self']
        ruler_enemy = self.game_data['ruler_enemy']
        enemy_chosen_color = self.game_data['enemy_chosen_color']

        return_color = -1

        '''
        TO - DO
        '''

        if ruler_self == 1:
            my_color = self.color_array[start_point_x[0]][start_point_y[0]]
        elif ruler_self == 2:
            my_color = self.color_array[start_point_x[1]][start_point_y[1]]

        return_color = random.randint(1, 6)
        while return_color == enemy_chosen_color or return_color == my_color:
            return_color = random.randint(1, 6)

        output_data = {'chosen_color': return_color}
        return output_data
