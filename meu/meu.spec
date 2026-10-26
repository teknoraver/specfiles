Name:           meu
Version:        0.1
Release:        2%{?dist}
Summary:        M3U Editor Utility, a simple editor for .m3u playlists

License:        GPL-3.0-or-later
URL:            https://github.com/teknoraver/meu
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  desktop-file-utils

# the SVG application icon is loaded through the Qt SVG icon engine plugin
%if 0%{?suse_version}
Requires:       libQt6Svg6
%else
Requires:       qt6-qtsvg
%endif
Requires:       hicolor-icon-theme

%description
Meu is a simple Qt application to create and edit .m3u playlists, for example
to organize the songs on a USB stick for the car stereo.
Songs can be added with a file dialog or by dragging files and directories,
sorted by path or by file name, and saved with paths relative to the playlist.
Files missing from an opened playlist are highlighted and not written back.

%prep
%autosetup

%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Tue Oct 27 2026 Matteo Croce <technoboy85@gmail.com> - 0.1-2
- Fix the Qt SVG dependency on openSUSE

* Mon Oct 26 2026 Matteo Croce <technoboy85@gmail.com> - 0.1-1
- First release
