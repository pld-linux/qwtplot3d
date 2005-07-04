Summary:	3D Graphics extension to the Qt GUI application framework
Summary(pl):	Rozszerzenie graficzne 3D do �rodowiska GUI Qt
Name:		qwtplot3d
Version:	0.2.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/qwtplot3d/%{name}-%{version}-beta.tgz
# Source0-md5:	063bcd47364b35be3c6182dca03be60d
URL:		http://qwt.sourceforge.net/
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%description -l pl
QwtPlot3D jest bogat� w mo�liwo�ci bibliotek� C++ opart� na Qt/OpenGL.
Udost�pnia w szczeg�lno�ci zestaw kontrolek 3D dla programist�w.

%package devel
Summary:	Header files for qwtplot3d library
Summary(pl):	Pliki nag��wkowe biblioteki qwtplot3d
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for qwtplot3d library.

%description devel -l pl
Pliki nag��wkowe biblioteki qwtplot3d.

%prep
%setup -q -n %{name}

%build
export QTDIR=%{_prefix}
qmake qwtplot3d.pro

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name},%{_libdir}}

for n in include/*.h ; do
    install -m 644 $n $RPM_BUILD_ROOT%{_includedir}/%{name}
done

for n in lib/libqwtplot3d.so* ; do
    cp -d $n $RPM_BUILD_ROOT%{_libdir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc examples
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}