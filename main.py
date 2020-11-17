

class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} мин'

    def __lt__(self, other):
        if not isinstance(other, Track):
            raise TypeError
        else:
            return self.duration < other.duration


class Album:
    def __init__(self, name, band, tracks=None):
        self.name = name
        self.band = band
        self.tracks = tracks or []

    def __str__(self):
        return f'Name group: {self.band} \n' \
               f'Name album: {self.name} \n' \
               f'Tracks: \n' \
               f'   ' + '\n   '.join(map(str, self.tracks))

    def get_tracks(self):
        for track in self.tracks:
            print(track)

    def add_track(self, track):
        if not isinstance(track, Track):
            raise TypeError
        else:
            self.tracks.append(track)

    def get_duration(self):
        print(sum(map(lambda track: int(track.duration), self.tracks)))


track1 = Track('track1', 3)
track2 = Track('track2', 2)
track3 = Track('track3', 4)
print(track1)
album1 = Album(name='album1', band='band', tracks=[track1, track2, track3])
album1.get_tracks()
album1.get_duration()


album2 = Album('album2', 'band')
album2.add_track(Track('track1', 3))
album2.add_track(Track('track2', 6))
album2.add_track(Track('trac3', 1))
album2.add_track(Track('track4', 4))
album2.get_tracks()
album2.get_duration()


print(album1)

print(track1 > track2)
