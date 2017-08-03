#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       harbour-infraview

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Examine network aspects of devices
Version:    0.1
Release:    7
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/a-dekker/infraview
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
# Requires:   nmap
Requires:   pyotherside-qml-plugin-python3-qt5 >= 1.3.0
Requires:   python3-base
Requires:   nmap-suid >= 7.50-3
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
InfraView lets you examine network aspects of devices


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/helper
%{_datadir}/%{name}/python
%attr(700,root,root) %{_datadir}/%{name}/python/netstat.py
%attr(755,root,root) %{_datadir}/%{name}/qml/pages/get_ip_address.sh
%attr(4755,root,root) %{_datadir}/%{name}/helper/infraview-helper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/icons/hicolor/108x108/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
/usr/bin
/usr/share/harbour-infraview
/usr/share/applications
/usr/share/icons/hicolor/86x86/apps
/usr/share/icons/hicolor/108x108/apps
/usr/share/icons/hicolor/128x128/apps
/usr/share/icons/hicolor/256x256/apps
