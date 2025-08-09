class Television:
    """
    A simple TV class with power, volume, channel, and mute functions.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Sets up the TV with power off, volume at 0, channel at 0, and not muted.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prev_volume: int = self.__volume

    def power(self) -> None:
        """
        Turns the TV on if it's off, or off if it's on.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes the TV if it’s not muted.
        Unmutes it and goes back to the old volume if it’s muted.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__prev_volume

    def channel_up(self) -> None:
        """
        Moves the channel up by 1.
        If it’s already at the max, it loops back to 0.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Moves the channel down by 1.
        If it’s already at 0, it loops back to the max channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Turns the volume up by 1, but not higher than the max.
        If muted, it unmutes first and restores the old volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__prev_volume = self.__volume

    def volume_down(self) -> None:
        """
        Turns the volume down by 1, but not lower than 0.
        If muted, it unmutes first and restores the old volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__prev_volume = self.__volume

    def __str__(self) -> str:
        """
        Shows the TV’s power, channel, and volume.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
