# Systemd PyDbus Example

Example setup for a pydbus service controllable via systemctl.

```
sudo pip install git+https://github.com/sezanzeb/systemd-pydbus-example.git
sudo systemctl daemon-reload
sudo systemctl start systemd-pydbus-example
```

The service is now running with root permissions and ready to receive
messages. Communicate with the server using the client:

```
systemd-pydbus-example-client --message hello
```

The service should have received the message and "hello" should now be
visible in:

```
systemctl status systemd-pydbus-example
```

## Resources

**.service files**

- [freedesktop.org docs](https://dbus.freedesktop.org/doc/dbus-daemon.1.html)

**pydbus**

- [LEW21/pydbus example](https://github.com/LEW21/pydbus/tree/cc407c8b1d25b7e28a6d661a29f9e661b1c9b964/examples/clientserver)

**PYTHONUNBUFFERED**

- [docs.python.org](https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED)
- [unix.stackexchange.com](https://unix.stackexchange.com/questions/285419/systemd-python-service-not-sending-all-output-to-syslog)

## License

Public Domain, do whatever you want with this code.
