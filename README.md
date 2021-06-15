<p align="center">
<a href="#"><img title="Welcome to Pentesting-Framework" src="https://user-images.githubusercontent.com/63346676/114345764-ef20fb00-9b7f-11eb-80a9-87db5953f5ea.png"></a>
</p>

![psfconsole](https://user-images.githubusercontent.com/63346676/119809462-c6bc4880-bf02-11eb-9756-0384878ead84.jpeg)

[![Open in Cloud Shell](https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/abhackerofficial/pentesting-framework&tutorial=README.md) [![Run on Repl.it](https://user-images.githubusercontent.com/27065646/92304596-bf719b00-ef7f-11ea-987f-2c1f3c323088.png)](https://repl.it/github/abhackerofficial/pentesting-framework)

> **[`Disclaimer`](#)**

The use of the `Psfconsole/pentesting-framework` and/or its resources is complete responsibility of the end-user. Developers assume no liabiity and are not responsible for any misuse or damage caused by `Psfconsole/pentesting-framework`. Some of your actions may be illegal and you can not use this software to test someone without written permission from person or company.

> **[`Installation`](#)**

**Installation method of psfconsole in your terminal.**

```bash <(curl -sL git.io/pSf) --install```

> **[`Dependencies`](#)**

`Psfconsole` requires following packages to run properly - 
- `jq`
- `php`
- `curl`
- `clang`
- `git`
- `subversion`
- `python2`
- `python3`

> **[`Psf Commands`](#)**

  ```
Console Commands

show     -   Command to displays option of a given type.
quit     -   Command to exit psfconsole instance.
clear    -   Command to clear screen.
help     -   Command to show help meunu.
search   -   Command to search available module.
banner   -   Command to shows a random banner.
history  -   Command to show command history.
version  -   Command to show the framework version.


Module Commands

use      -   Command to call existing modules.
list     -   Command to show available options
info     -   Command to information about modules.
back     -   Command to move back to main console.
  ```

> Console Command Usages.

usage of `show modules` command in console.

```bash
psf > show modules
....

Usage: use with:<module>/<submodule>/handler

....

Examples:
  use with:secure/hashes/handler
```

usage of `quit` command in console.
```bash
psf > quit
(>) Existing Psfconsole ...
```

usage of `search` command in console.
```bash
psf > search
Usage: search module:<module>
       search submodule:<submodule>

 Examples:
  search module:lookup
  search submodule:user
```

usage of `history` command in console.
```bash
psf > history
1  show modules
2  quit
3  search
4  history
```

> Module Command Usages.

usage of `use` command in module.
```bash
psf > use with:secure/hashes/handler
(>) Using configured with:secure/hashes mode
psf use(program/secure/hashes) >
```

usage of `info` command in modules.
```bash
psf use(program/secure/hashes) > info

Name: hashes
Module: withSECURE/HASHES
Internet Required: not

Description:
  module to generate hashing algorithm.
```

usage of `back` command in module.

```bash
psf use(program/secure/hashes) > back
psf >
```

usage of `list` command in module.
```bash
psf use(program/secure/hashes) > list

(01) Md5sum
(02) Sha1sum
(03) Sha224sum
(04) Sha256sum
(05) Sha384sum
(06) Sha512sum
(07) Shasum
(08) Base64
(09) Base32
```

> **[`Maintainer`](#)**

This [pentesting-framework](https://github.com/abhackerofficial/pentesting-framework) is maintained by the following person.

<p align="center">
<a href="https://paypal.me/abhackerofficial"><img title="Donation" src="https://user-images.githubusercontent.com/74892618/104415238-a618d500-5597-11eb-82a4-46b7c1913e2c.png"></a>
</p>

| ![ABHacker Official](https://user-images.githubusercontent.com/63346676/97066596-3f0d0500-15d4-11eb-9cb3-b7ed5206c6f6.png) |
| ----------------------------------------------------------------------------------------------------- |
| <p align="center"> [ABHacker Official](https://github.com/abhackerofficial)                                                   |</p>

> [`Contributors`](https://github.com/abhackerofficial/pentesting-framework/blob/master/CONTRIBUTE.md) [`Creditors`](https://github.com/abhackerofficial/pentesting-framework/blob/master/CREDIT.md)

Pentesting-Framework has a vibrant community of happy users and delightful contributors and creditors. Without all the time and help from our contributors, it wouldn't be so awesome.

Thank you so much!
