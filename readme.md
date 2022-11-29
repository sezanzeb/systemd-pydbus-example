# Systemd PyDbus Example

Example setup for a pydbus service controllable via systemctl.

```bash
git clone https://github.com/sezanzeb/systemd-pydbus-example
cd systemd-pydbus-example
sudo python3 setup.py install
sudo systemctl daemon-reload
sudo systemctl start systemd-pydbus-example
```

The service is now running with root permissions and ready to receive
messages. Communicate with the server using the client:

```bash
systemd-pydbus-example-client --message hello
```

The service should have received the message and "hello" should now be
visible in:

```bash
systemctl status systemd-pydbus-example
```

## Resources

**.service files**

- [freedesktop.org](https://dbus.freedesktop.org/doc/dbus-daemon.1.html)
- [wiki.archlinux.org](https://wiki.archlinux.org/index.php/Systemd)

**pydbus**

- [LEW21/pydbus example](https://github.com/LEW21/pydbus/tree/cc407c8b1d25b7e28a6d661a29f9e661b1c9b964/examples/clientserver)

**PYTHONUNBUFFERED**

- [docs.python.org](https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED)
- [unix.stackexchange.com](https://unix.stackexchange.com/questions/285419/systemd-python-service-not-sending-all-output-to-syslog)

## License

Public Domain, do whatever you want with this code.
