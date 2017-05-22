# Based on the currency of India
# Taken into account only Rs, We have stopped dealing in Paise's

def change_calcualtor(payable_amount, payed_amount):
    return_amount = payed_amount - payable_amount
    notes = [2000, 500, 100, 50, 20, 10, 5, 2, 1]
    return_amount_breakup = {}
    note_index = 0
    track_amount = return_amount
    while track_amount > 0:
        if track_amount < notes[note_index]:
            note_index += 1
            continue
        else:
            return_amount_breakup[notes[note_index]] = track_amount // \
                                                        notes[note_index]
            track_amount = track_amount % notes[note_index]
            note_index += 1
    return return_amount_breakup, return_amount
