def consumption(sessions, selected):
    values = {release: [] for release in selected}
    for row in sessions:
        if row['release'] in selected and row['consented']:
            values[row['release']].append(row['seconds'])
    return {release: {'eligible': len(seconds), 'seconds': sum(seconds)} for release, seconds in values.items()}


def questionnaire(cohorts, market):
    relevant = [row for row in cohorts if row['market'] == market]
    return {'invited': sum(row['invited'] for row in relevant),
            'responded': sum(row['responded'] for row in relevant)}
