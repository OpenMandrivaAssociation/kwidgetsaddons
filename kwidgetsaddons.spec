%define major 5
%define libname %mklibname KF5GuiAddons %{major}
%define devname %mklibname KF5GuiAddons -d
%define debug_package %{nil}

Name: kwidgetsaddons
Version: 4.95.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Widgets Library addons
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 Widgets Library addons

%package -n %{libname}
Summary: The KDE Frameworks 5 Widgets Library addons
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 Widgets Library addons

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_datadir}/kcharselect

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5WidgetsAddons
