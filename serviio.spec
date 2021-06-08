%define debug_package %nil
Name: serviio
Version: 2.1
Release: alt1
License: Freeware
Summary: A free media server
Url: https://download.serviio.org/releases/
Group: Networking/Other
Source: serviio-%version-linux.tar.gz
Source1: serviio.service
Source3: serviio.png
BuildRequires: tar
BuildRequires: gzip
BuildRequires: systemd
Requires: ffmpeg
Requires: x264
Requires: lame
Requires: dcraw
Requires: java >= 1.8.0

%description
It allows you to stream your media files (music, video
or images) to renderer devices (e.g. a TV set, Bluray player, games console
or mobile phone) on your connected home network.

%files
%doc legal/{*.txt,*.xerox} *.txt
%_iconsdir/%name.png
%_unitdir/serviio.service
%dir %_datadir/java/serviio
%dir %_datadir/java/serviio/bin
%dir %_datadir/java/serviio/config
%dir %_datadir/java/serviio/lib
%dir %_datadir/java/serviio/library
%dir %_datadir/java/serviio/plugins
%_datadir/java/serviio/bin/*.sh
%_datadir/java/serviio/config/*.xml
%_datadir/java/serviio/lib/*.jar
%_datadir/java/serviio/plugins/*.txt
%_datadir/java/serviio/library/derby.properties
%_datadir/applications/%name.desktop

%pre
getent group serviio >/dev/null || groupadd -r serviio
   useradd -r -g serviio -d %_datadir/java/serviio -s /sbin/nologin \
   -c "A free media server" serviio
exit 0

%post
 %post_service %name

%preun
%preun_service %name

#----------------------------------------------------------------

%prep
%setup -q

%build
%install
install -d %buildroot%_datadir/{java/serviio/bin,java/serviio/config,java/serviio/lib,java/serviio/library,java/serviio/plugins,java/serviio/log}
install -m 0755 bin/*.sh %buildroot%_datadir/java/serviio/bin
install -m 644 config/*.xml %buildroot%_datadir/java/serviio/config
install -m 644 lib/*.jar %buildroot%_datadir/java/serviio/lib
install -m 644 library/derby.properties %buildroot%_datadir/java/serviio/library
install -m 644 plugins/plugins-readme.txt %buildroot%_datadir/java/serviio/plugins
install -Dm 644 %SOURCE1 %buildroot%_unitdir/%name.service
install -Dm 644 %SOURCE3 %buildroot%_iconsdir/%name.png
install -d %buildroot%_datadir/applications

cat > %buildroot%_datadir/applications/%name.desktop << EOF
[Desktop Entry]
Name=serviio
Icon=%name
Comment=A free media server
Comment [ru]= Бесплатный медиасервер
URL=http://localhost:23423/console
Type=Link
Categories=AudioVideo;
EOF

%changelog
* Tue Jun 08 2021 Nikolaj Sabelnikov <saber@altlinux.ru> 2.1-alt1
- 

