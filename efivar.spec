Name:           efivar
Version:        37
Release:        6
Summary:        Tools and libraries to work with EFI variables
License:        LGPLv2.1
URL:            https://github.com/rhboot/%{name}
Source0:        https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0001:      first-fix-gcc9-new-waring.patch
Patch0002:      second-fix-gcc9-new-waring.patch

BuildRequires:  popt-devel glibc-static
BuildRequires:  gcc
Requires:       %{name}-libs = %{version}-%{release}

%description
Some command line interface of the UEFI variables tools are offered by %{name}.

%package        libs
Summary:        Libraries for %{name}

%description    libs
Libraries for %{name}.

%package        devel
Summary:        Development headers requred by libefivar
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
Development titles to use libefivar must be included.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
export LDFLAGS="-flto-partition=none"
%make_build

%install
%make_install

%ldconfig_scriptlets libs

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/%{name}

%files libs
%defattr(-,root,root)
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
* Fri Jul 30 2021 gaihuiying <gaihuiying1@huawei.com> - 37-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix build error with gcc10

* Thu May 27 2021 lijingyuan <lijingyuan3@huawei.com> - 37-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Add the compilation dependency of gcc.

* Yue Jun 9 2020 zhujunhao <zhujunhao8@huawei.com> - 37-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix gcc9 new warning -Werror=address-of-packed-member

* Mon Feb 17 2020 hexiujun <hexiujun1@huawei.com> - 37-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:unpack libs subpackage

* Thu Oct 17 2019 openEuler Buildteam <buildteam@openeuler.org> - 37-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:remove the libabigail in buildRequires.

* Mon Sep 2 2019 openEuler Buildteam <buildteam@openeuler.org> - 37-1
- Package init
