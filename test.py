def solution1(A, B, S):
    slot_to_patient = {}

    for i in range(len(A)):
        if A[i] in slot_to_patient and B[i] in slot_to_patient:
            return False
        if A[i] in slot_to_patient:
            slot_to_patient[B[i]] = i
        elif B[i] in slot_to_patient:
            slot_to_patient[A[i]] = i
        else:
            slot_to_patient[A[i]] = i

    return len(slot_to_patient) <= S
