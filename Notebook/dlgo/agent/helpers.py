from dlgo.gotypes import Point

def is_point_an_eye(board, point, color):
    if board.get(point) is not None:
        return False
    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False
    
    friendly_coners = 0
    off_board_corners =0
    corners = [
        Point(point.row -1, point.col -1),
        Point(point.row -1, point.col +1),
        Point(point.row +1, point.col -1),
        Point(point.row +1, point.col +1),
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_corlor = board.get(corner)
            if corner_corlor == color:
                friendly_coners += 1
            else:
                off_board_corners +=1
    
    if off_board_corners > 0:
        return off_board_corners + friendly_coners == 4
    return friendly_coners >=3