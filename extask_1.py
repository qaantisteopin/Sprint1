types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}
tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}


def delete_duplicates(tickets_dict):
    result = tickets_dict.copy()
    seen_tickets = []

    for priority in sorted(result.keys()):
        tickets_to_keep = []

        for ticket in result[priority]:
            if ticket not in seen_tickets:
                tickets_to_keep.append(ticket)
                seen_tickets.append(ticket)

        result[priority] = tickets_to_keep

    return result


def create_dict(types_dict, tickets_dict):
    tickets_by_type = {}
    for key in sorted(types_dict.keys()):
        tickets_by_type[types_dict[key]] = tickets_dict[key]
    return tickets_by_type


tickets_dict_without_duplicates = delete_duplicates(tickets)
tickets_result = create_dict(types, tickets_dict_without_duplicates)
print(tickets_result)
