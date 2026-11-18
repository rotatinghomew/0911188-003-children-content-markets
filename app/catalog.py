def in_window(release, day):
    return release['starts'] <= day and (release['ends'] is None or day < release['ends'])


def offered(releases, market, day):
    return {row['id']: row for row in releases if row['market'] == market and in_window(row, day)}
