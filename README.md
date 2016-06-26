# pyninjasphere

A NinjaSphere client that is written primarily for use with home-assistent

## Home-assistent

See https://github.com/keerts/home-assistant/tree/ninja-sphere

## Command line interface

You can use the command line interface to quickly check the status of the things on your NinjaSphere:

```
> pyninjasphere list -h 192.168.192.33
Listing things from host 192.168.192.33.
{'promoted': True, 'name': 'Spot 3', 'location': 'c1350e2a-41cd-345g-9da9-0d3919359920', 'id': '4e1175ae-0885-4194-a46e-2af88e278934', 'device': <Device: Device object>, 'deviceId': 'e301f883fa', 'type': 'light'}
{'promoted': True, 'name': 'Xmas Tree', 'location': 'c1350e2a-41cd-345g-9da9-0d3919359920', 'id': 'bc967c53-669e-409c-92ef-49f3470ddfaf', 'device': <Device: Device object>, 'deviceId': 'ef23c63470', 'type': 'xmastree'}
{'promoted': False, 'name': 'Chromecast Chromecast\\ TV._googlecast._tcp.local.', 'location': None, 'id': 'b3ee2202-46b0-4d6f-af1d-5754033cd379', 'device': <Device: Device object>, 'deviceId': '944d8fc4df', 'type': 'mediaplayer'}
{'promoted': False, 'name': 'Spheramid UWTKRHGJPCQCK', 'location': 'c1350e2a-41cd-345g-9da9-0d3919359920', 'id': 'UWTKRHGJPCQCK', 'device': <Device: Device object>, 'deviceId': '889e28e85d', 'type': 'node'}
{'promoted': False, 'name': 'Spot 2', 'location': None, 'id': 'cee13521-fa45-4559-9f87-60882e26287e', 'device': <Device: Device object>, 'deviceId': 'be5a23604d', 'type': 'light'}
{'promoted': True, 'name': 'Spot 1', 'location': 'c1350e2a-41cd-345g-9da9-0d3919359920', 'id': 'a137c933-cb48-4eff-80c8-ea81e279e377', 'device': <Device: Device object>, 'deviceId': 'b35628d81b', 'type': 'light'}
{'promoted': False, 'name': 'Nexus 4', 'location': None, 'id': '5a0fee16-6918-409a-b6e2-fa1aecc5a461', 'device': <Device: Device object>, 'deviceId': '8a918feac0', 'type': 'mobile'}
```

## Acknowledgements

Thanks @ronneke1996 et al for creating the largest parts of the module and providing a pull request.
