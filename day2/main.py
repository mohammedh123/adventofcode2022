from enum import Enum


class RoundResult(Enum):
    DRAW = 'Y'
    LOSS = 'X'
    WIN = 'Z'


class ShapeType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


SHAPE_TO_SCORE = {
    ShapeType.ROCK: 1,
    ShapeType.PAPER: 2,
    ShapeType.SCISSORS: 3,
}


RESULT_TO_SCORE = {
    RoundResult.DRAW: 3,
    RoundResult.LOSS: 0,
    RoundResult.WIN: 6,
}


VICTORY_CONDITION_BY_SHAPE = {
    ShapeType.ROCK: ShapeType.SCISSORS,
    ShapeType.PAPER: ShapeType.ROCK,
    ShapeType.SCISSORS: ShapeType.PAPER,
}


CHR_TO_SHAPE = {
    'A': ShapeType.ROCK,
    'X': ShapeType.ROCK,
    'B': ShapeType.PAPER,
    'Y': ShapeType.PAPER,
    'C': ShapeType.SCISSORS,
    'Z': ShapeType.SCISSORS,
}


LOSS_CONDITION_BY_SHAPE = {v: k for k, v in VICTORY_CONDITION_BY_SHAPE.items()}  # Inverted victory mapping


def calculate_score_from_rounds(rounds):
    total_score = 0
    result = RoundResult.DRAW
    for opponent, player in rounds:
        if player == opponent:
            result = RoundResult.DRAW
        elif opponent == VICTORY_CONDITION_BY_SHAPE[player]:
            result = RoundResult.WIN
        else:
            result = RoundResult.LOSS

        total_score += SHAPE_TO_SCORE[player] + RESULT_TO_SCORE[result]

    return total_score


def decrypt_strategy_guide(strategy_guide):
    rounds = []
    for opponent_chr, desired_round_result in strategy_guide:
        opponent = CHR_TO_SHAPE[opponent_chr]

        match RoundResult(desired_round_result):
            case RoundResult.DRAW:
                rounds.append((opponent, opponent))
            case RoundResult.WIN:
                rounds.append((opponent, LOSS_CONDITION_BY_SHAPE[opponent]))
            case RoundResult.LOSS:
                rounds.append((opponent, VICTORY_CONDITION_BY_SHAPE[opponent]))

    return rounds


with open('input') as f:
    strategy_guide = [tuple(line.strip().split()) for line in f]

rounds = [(CHR_TO_SHAPE[opponent_chr], CHR_TO_SHAPE[player_chr]) for opponent_chr, player_chr in strategy_guide]
print(f'Part 1: {calculate_score_from_rounds(rounds)}')

desired_rounds = decrypt_strategy_guide(strategy_guide)
print(f'Part 2: {calculate_score_from_rounds(desired_rounds)}')
