# see m4/${libname}.m4 />= for required version of particular library
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libcpath_ver	20180716
%define		libcsplit_ver	20120701
%define		libcthreads_ver	20160404
%define		libuna_ver	20230702
Summary:	Library to support various Hash-based Message Authentication Codes (HMAC)
Summary(pl.UTF-8):	Biblioteka obsługująca różne kody uwierzytelniające oparte na skrótach (HMAC)
Name:		libhmac
Version:	20240417
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libhmac/releases
Source0:	https://github.com/libyal/libhmac/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	5c93ed2bb4dbeef646b0e2f2f4c753c6
URL:		https://github.com/libyal/libhmac/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libuna >= %{libuna_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libhmac is a library to support various Hash-based Message
Authentication Codes (HMAC).

%description -l pl.UTF-8
libhmac to biblioteka obsługująca różne kody uwierzytelniające oparte
na skrótach (HMAC - Hash-based Message Authentication Codes).

%package devel
Summary:	Header files for libhmac library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libhmac
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	openssl-devel >= 1.0

%description devel
Header files for libhmac library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libhmac.

%package static
Summary:	Static libhmac library
Summary(pl.UTF-8):	Statyczna biblioteka libhmac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libhmac library.

%description static -l pl.UTF-8
Statyczna biblioteka libhmac.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhmac.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/hmacsum
%attr(755,root,root) %{_libdir}/libhmac.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhmac.so.1
%{_mandir}/man1/hmacsum.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhmac.so
%{_includedir}/libhmac
%{_includedir}/libhmac.h
%{_pkgconfigdir}/libhmac.pc
%{_mandir}/man3/libhmac.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhmac.a
