"""Cal.diy: show the month and that day's times side by side from 480px up (upstream: 768px).
Run from the cal.diy source root. Every replacement must match exactly once."""
import sys

EDITS = [
    ("packages/features/bookings/Booker/hooks/useBookerLayout.ts",
     'const isMobile = useMediaQuery("(max-width: 768px)");',
     'const isMobile = useMediaQuery("(max-width: 479px)");'),
    ("packages/embeds/embed-core/src/embed-iframe/react-hooks.ts",
     'const isMobile = useMediaQuery("(max-width: 768px)");',
     'const isMobile = useMediaQuery("(max-width: 479px)");'),
    ("packages/features/bookings/Booker/config.ts",
     '"[--booker-timeslots-width:240px] lg:[--booker-timeslots-width:280px]"',
     '"[--booker-timeslots-width:192px] md:[--booker-timeslots-width:240px] lg:[--booker-timeslots-width:280px]"'),
    ("apps/web/modules/bookings/components/Booker.tsx",
     '"h-full overflow-hidden md:w-(--booker-timeslots-width)"',
     '"h-full overflow-hidden border-l w-(--booker-timeslots-width)"'),
    ("apps/web/modules/bookings/components/AvailableTimeSlots.tsx",
     'limitHeight && "no-scrollbar grow overflow-auto md:h-[400px]"',
     'limitHeight && "no-scrollbar grow overflow-auto h-[400px]"'),
    # "Mon 23" above the times stays on one line beside the 12h/24h switch
    ("apps/web/modules/bookings/components/AvailableTimesHeader.tsx",
     'isColumnView ? "text-subtle text-xs uppercase" : "text-emphasis font-semibold"',
     'isColumnView ? "text-subtle text-xs uppercase" : "text-emphasis whitespace-nowrap font-semibold"'),
    # the "DEC" tag on the first day of the next month: small, centred, above the number instead of over it
    ("packages/features/calendars/components/DatePicker.tsx",
     '"absolute top-0 z-10 mx-auto w-fit rounded-full font-semibold uppercase tracking-wide",',
     '"pointer-events-none absolute left-0 right-0 top-0 z-10 mx-auto w-fit rounded-full font-semibold uppercase tracking-wide",'),
    ("packages/features/calendars/components/DatePicker.tsx",
     '''            fontSize: "10px",
            lineHeight: "13px",
            padding: disabled ? "0 3px" : "3px 3px 3px 4px",''',
     '''            fontSize: "8px",
            lineHeight: "9px",
            padding: "2px 2px 0",'''),
]
for path, old, new in EDITS:
    src = open(path, encoding="utf-8").read()
    n = src.count(old)
    if n != 1:
        sys.exit(f"{path}: expected 1 match, found {n}: {old}")
    open(path, "w", encoding="utf-8").write(src.replace(old, new))
    print("patched", path)
