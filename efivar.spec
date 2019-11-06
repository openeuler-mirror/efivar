Name:           efivar
Version:        37
Release:        2
Summary:        Tools and libraries to work with EFI variables
License:        LGPLv2.1
URL:            https://github.com/rhboot/%{name}
Source0:        https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  popt-devel glibc-static
Provides:       %{name}-libs
Obsoletes:      %{name}-libs

%description
Some command line interface of the UEFI variables tools are offered by %{name}.

%package        devel
Summary:        Development headers requred by libefivar
Requires:       %{name} = %{version}-%{release}

%description    devel
Development titles to use libefivar must be included.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/%{name}
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libefiboot.so
%{_libdir}/libefivar.so

%files help
%defattr(-,root,root)
%doc README.md
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man3/*

%changelog
* Thu Oct 17 2019 openEuler Buildteam <buildteam@openeuler.org> - 37-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:remove the libabigail in buildRequires.

* Mon Sep 2 2019 openEuler Buildteam <buildteam@openeuler.org> - 37-1
- Package init
