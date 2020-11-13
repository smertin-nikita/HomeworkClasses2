

class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'{self.name} - {self.duration} мин')


class Album:
    def __init__(self, name, band, tracks=None):
        self.name = name
        self.band = band
        self.tracks = tracks or []

    def get_tracks(self):
        for track in self.tracks:
            track.show()

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        print(sum(map(lambda track: int(track.duration), self.tracks)))


album1 = Album(name='album1', band='band', tracks=[Track('track1', 3)])
album1.get_tracks()
album1.get_duration()


album2 = Album('album2', 'band')
album2.add_track(Track('track1', 3))
album2.add_track(Track('track2', 6))
album2.add_track(Track('trac3', 1))
album2.add_track(Track('track4', 4))
album2.get_tracks()
album2.get_duration()
