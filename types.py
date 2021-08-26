class USCaseMeta:
    def __init__(self, case_id, docket_number, self_cite, circuit_name, date, tags):
        self.case_id = case_id
        self.docket_number = docket_number
        self.self_cite = self_cite
        self.circuit_name = circuit_name
        self.date = date
        self.tags = tags
        pass

class USJudge:
    def __init__(self, name, orig_name, gender, party):
        pass

class JudgeRuling:
    def __init__(self, judge_id, case_id, author, vote):
        pass