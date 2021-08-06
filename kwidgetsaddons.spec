%define major 5
%define libname %mklibname KF5WidgetsAddons %{major}
%define devname %mklibname KF5WidgetsAddons -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwidgetsaddons
Version: 5.85.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Widgets Library addons
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5UiTools)
# For Python bindings
BuildRequires: cmake(PythonModuleGeneration)
BuildRequires: pkgconfig(python3)
BuildRequires: python-qt5-core
BuildRequires: python-qt5-gui
BuildRequires: python-qt5-widgets
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 Widgets Library addons.

%package -n %{libname}
Summary: The KDE Frameworks 5 Widgets Library addons
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 Widgets Library addons.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package -n python-%{name}
Summary: Python bindings for %{name}
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n python-%{name}
Python bindings for %{name}

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%files designer
%{_libdir}/qt5/plugins/designer/kwidgetsaddons5widgets.so

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

[ -s %{buildroot}%{python_sitearch}/PyKF5/__init__.py ] || rm -f %{buildroot}%{python_sitearch}/PyKF5/__init__.py

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

# Let's not ship py2 crap unless and until something still needs it...
rm -rf %{buildroot}%{_libdir}/python2*

%files -f %{name}.lang
%{_datadir}/kf5/kcharselect
%{_datadir}/qlogging-categories5/kwidgetsaddons.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%(echo %{version}|cut -d. -f1-2).0

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5WidgetsAddons
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

%files -n python-%{name}
%dir %{python_sitearch}/PyKF5
%{python_sitearch}/PyKF5/KWidgetsAddons.so
%dir %{_datadir}/sip/PyKF5
%{_datadir}/sip/PyKF5/KWidgetsAddons
