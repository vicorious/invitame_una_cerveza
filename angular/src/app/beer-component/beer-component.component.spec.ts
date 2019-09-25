import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BeerComponentComponent } from './beer-component.component';

describe('BeerComponentComponent', () => {
  let component: BeerComponentComponent;
  let fixture: ComponentFixture<BeerComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BeerComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BeerComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
