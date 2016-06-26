### This file is an attempt to create a class to run DMA PWM based on gpiozero library
# It's not working currently  


import gpiozero
from gpiozero import PWMOutputDevice


class Servo(PWMOutputDevice):
    """
    Extends :class:`PWMOutputDevice` and represents a hobby servo, which can be
    instructed to rotate to a given angle.
    A typical configuration of such a device is to connect it to 5V, GND and a
    single GPIO pin. The servo is controlled by sending a pulse signal which
    determines the angle the device should rotate to.
    :param int pin:
        The GPIO pin which the servo is attached to. See :doc:`notes` for
        valid pin numbers.
    :param float initial_value:
        XXX
    :param float initial_angle:
        XXX
    :param int frequency:
        The frequency (in Hz) of pulses emitted to drive the LED. Defaults
        to 100Hz.
    :param int max_angle:
        The maximum angle the servo can rotate to. Defaults to 180 degrees.
    :param int min_duty_cycle:
        The duty cycle required to set the servo to a 0 degree angle.
    :param int max_duty_cycle:
        The duty cycle required to set the servo to its maximum angle.
        max_angle=180, min_duty_cycle=0.033,
        max_duty_cycle=0.254
    """
    def __init__(self, pin=None, initial_value=0, initial_angle=None,
                frequency=100, max_angle=180, min_duty_cycle=0.033,
                max_duty_cycle=0.254):
        active_high = True
        self._max_angle = max_angle
        self._min_duty_cycle = min_duty_cycle
        self._max_duty_cycle = max_duty_cycle
        super(Servo, self).__init__(pin, active_high, initial_value, frequency)

    @property
    def value(self):
        """
        The proportion of the potential angle the servo is currently positioned.
        0.0 is 0 degrees, 1.0 is the maximum angle. Values in between may be
        specified for varying positions proportionally between 0 and the maximum
        angle.
        """
        duty_cycle = self._read()
        value = (
            (duty_cycle - self._min_duty_cycle) /
            (self._max_duty_cycle - self._min_duty_cycle)
        )
        return value

    @value.setter
    def value(self, value):
        self.angle = value * self._max_angle

    @property
    def angle(self):
        """
        The angle the servo is currently positioned. Value will be between 0
        and max_angle.
        """
        return self._angle

    @angle.setter
    def angle(self, value):
        if not 0 <= value <= self._max_angle:
            raise OutputDeviceBadValue(
                "angle must be between 0 and %s" % self._max_angle
            )
        self._angle = value
        duty_cycle = (
            (self._max_duty_cycle - self._min_duty_cycle)
            * value / self._max_angle
        ) + self._min_duty_cycle
        self._write(duty_cycle)

