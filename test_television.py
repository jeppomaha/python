import pytest
from television import Television

def test_init():
    """Check starting values for TV."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    """Check TV on/off states."""
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)  # TV on
    tv.power()
    assert "Power = False" in str(tv)  # TV off

def test_mute():
    """Check muting and unmuting in different states."""
    tv = Television()
    
    # TV on, volume up, then mute
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    
    # TV on and unmute
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    
    # TV off and mute (should do nothing)
    tv.power()
    tv.mute()
    assert "Power = False" in str(tv)

def test_channel_up():
    """Check channel up in all scenarios."""
    tv = Television()
    
    # Off and channel up (should not change)
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
    # On and channel up
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)
    
    # On and wrap past max
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down():
    """Check channel down in all scenarios."""
    tv = Television()
    
    # Off and channel down (should not change)
    tv.channel_down()
    assert "Channel = 0" in str(tv)
    
    # On and wrap below min
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)

def test_volume_up():
    """Check volume up in all scenarios."""
    tv = Television()
    
    # Off and volume up (should not change)
    tv.volume_up()
    assert "Volume = 0" in str(tv)
    
    # On and volume up
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)
    
    # On, muted, and volume up (should restore)
    tv.mute()
    tv.volume_up()
    assert "Volume = 2" in str(tv)
    
    # On and past max
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_down():
    """Check volume down in all scenarios."""
    tv = Television()
    
    # Off and volume down (should not change)
    tv.volume_down()
    assert "Volume = 0" in str(tv)
    
    # On, raise volume to max, then down
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert "Volume = 1" in str(tv)
    
    # On, muted, and volume down (should restore then lower)
    tv.mute()
    tv.volume_down()
    assert "Volume = 0" in str(tv)
    
    # On and past min
    tv.volume_down()
    assert "Volume = 0" in str(tv)
